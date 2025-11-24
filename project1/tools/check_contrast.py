from __future__ import annotations
import re
import os
import sys
from math import pow
from typing import Optional, Tuple

# WCAG contrast helpers + simple CSS scanner

NAMED_COLORS = {
    'white': '#ffffff',
    'black': '#000000',
    'transparent': None,
}


def hex_to_rgb_tuple(s: str) -> Tuple[int, int, int]:
    s = s.strip()
    if s.startswith('#'):
        s = s[1:]
    if len(s) == 3:
        s = ''.join([c * 2 for c in s])
    return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))


def parse_rgb(s: str) -> Tuple[int, int, int, Optional[float]]:
    s = s.strip()
    if s.startswith('#'):
        r, g, b = hex_to_rgb_tuple(s)
        return (r, g, b, 1.0)
    if s.startswith('rgba'):
        m = re.match(r'rgba\s*\(([^)]+)\)', s)
        if not m:
            raise ValueError('invalid rgba')
        parts = [p.strip() for p in m.group(1).split(',')]
        r, g, b = [int(float(x)) for x in parts[:3]]
        a = float(parts[3]) if len(parts) > 3 else 1.0
        return (r, g, b, a)
    if s.startswith('rgb'):
        m = re.match(r'rgb\s*\(([^)]+)\)', s)
        parts = [p.strip() for p in m.group(1).split(',')]
        r, g, b = [int(float(x)) for x in parts[:3]]
        return (r, g, b, 1.0)
    key = s.lower()
    if key in NAMED_COLORS and NAMED_COLORS[key] is not None:
        r, g, b = hex_to_rgb_tuple(NAMED_COLORS[key])
        return (r, g, b, 1.0)
    raise ValueError(f'unrecognized color: {s}')


def blend_rgba_over_bg(fg_rgb: Tuple[int, int, int, float], bg_rgb: Tuple[int, int, int]) -> Tuple[int, int, int]:
    fr, fg, fb, a = fg_rgb
    br, bg, bb = bg_rgb
    a = a if a is not None else 1.0
    rr = int(round(fr * a + br * (1 - a)))
    rg = int(round(fg * a + bg * (1 - a)))
    rb = int(round(fb * a + bb * (1 - a)))
    return (rr, rg, rb)


def linearize(c: float) -> float:
    if c <= 0.03928:
        return c / 12.92
    return pow((c + 0.055) / 1.055, 2.4)


def luminance(rgb: Tuple[int, int, int]) -> float:
    r, g, b = rgb
    return 0.2126 * linearize(r / 255.0) + 0.7152 * linearize(g / 255.0) + 0.0722 * linearize(b / 255.0)


def contrast_ratio(fg_rgb: Tuple[int, int, int], bg_rgb: Tuple[int, int, int]) -> float:
    L1 = luminance(fg_rgb)
    L2 = luminance(bg_rgb)
    lighter = max(L1, L2)
    darker = min(L1, L2)
    return (lighter + 0.05) / (darker + 0.05)


def extract_rules(css_text: str):
    # crude rule extraction: selectors { declarations }
    pattern = re.compile(r'([^{}]+)\{([^}]+)\}')
    for m in pattern.finditer(css_text):
        selector = m.group(1).strip()
        decls = m.group(2).strip()
        yield selector, decls


def find_body_bg(css_text: str) -> Optional[str]:
    for sel, decls in extract_rules(css_text):
        if re.match(r'(^|[,\s])body($|[,\s])', sel) or sel.strip() == 'body':
            m = re.search(r'background(?:-color)?\s*:\s*([^;]+);', decls)
            if m:
                return m.group(1).strip()
    return None


def analyze_css_file(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()

    body_bg_raw = find_body_bg(txt)
    body_bg_rgb = None
    if body_bg_raw:
        try:
            r, g, b, a = parse_rgb(body_bg_raw)
            body_bg_rgb = (r, g, b)
        except Exception:
            body_bg_rgb = None

    if body_bg_rgb is None:
        # fallback common site bg
        body_bg_rgb = hex_to_rgb_tuple('#f9f4ef')

    results = []
    for sel, decls in extract_rules(txt):
        color_match = re.search(r'color\s*:\s*([^;]+);', decls)
        bg_match = re.search(r'background(?:-color)?\s*:\s*([^;]+);', decls)
        if color_match:
            color_raw = color_match.group(1).strip()
            # select background candidate: declared background, gradient or body
            bg_raw = bg_match.group(1).strip() if bg_match else None
            # try to extract a hex from background (gradients etc.)
            bg_hex = None
            if bg_raw:
                m_hex = re.search(r'#([0-9a-fA-F]{3,6})', bg_raw)
                if m_hex:
                    bg_hex = '#' + m_hex.group(1)

            try:
                fg = parse_rgb(color_raw)
            except Exception:
                # unknown color name -> skip
                continue

            if fg[3] < 1.0 and bg_hex is None:
                # semi-transparent text over body
                bg_rgb = body_bg_rgb
            elif bg_hex:
                bg_rgb = hex_to_rgb_tuple(bg_hex)
            else:
                bg_rgb = body_bg_rgb

            if fg[3] < 1.0:
                blended = blend_rgba_over_bg(fg, bg_rgb)
                fg_rgb = blended
            else:
                fg_rgb = (fg[0], fg[1], fg[2])

            ratio = contrast_ratio(fg_rgb, bg_rgb)
            results.append({'selector': sel, 'color': color_raw, 'background': bg_raw or 'body', 'ratio': ratio})

    return {'path': path, 'body_bg': body_bg_rgb, 'issues': results}


def run_scan(root: str):
    css_files = []
    for dirpath, dirs, files in os.walk(root):
        for name in files:
            if name.lower().endswith('.css'):
                css_files.append(os.path.join(dirpath, name))

    summary = {}
    for css in sorted(css_files):
        res = analyze_css_file(css)
        fails = [r for r in res['issues'] if r['ratio'] < 4.5]
        summary[css] = {'total': len(res['issues']), 'fails': fails}
    return summary


def print_summary(summary: dict):
    total_files = len(summary)
    total_issues = 0
    total_fails = 0
    print(f"Scanned {total_files} CSS files\n")
    for path, data in summary.items():
        print(f"File: {path}")
        print(f"  color rules found: {data['total']}")
        if data['fails']:
            print(f"  FAILING rules ({len(data['fails'])}):")
            for f in data['fails']:
                total_fails += 1
                print(f"    selector: {f['selector'][:60]!r} color:{f['color']} bg:{f['background']} ratio:{f['ratio']:.2f}")
        else:
            print("  All color rules meet 4.5:1 contrast against their background/body where detectable.")
        total_issues += data['total']
        print()
    print(f"Summary: scanned {total_files} files, {total_issues} color rules, {total_fails} failing rules (<4.5).")


def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if len(sys.argv) > 1:
        root = sys.argv[1]
    summary = run_scan(root)
    print_summary(summary)


if __name__ == '__main__':
    main()
