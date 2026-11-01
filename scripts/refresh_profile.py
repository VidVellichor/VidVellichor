"""Generate a dated public-repository snapshot. No third-party widget service."""
import collections
import datetime
import html
import json
import os
import pathlib
import urllib.request

OWNER = 'VidVellichor'
ROOT = pathlib.Path(__file__).resolve().parents[1]

def get(path):
    headers = {'User-Agent': 'VidVellichor-profile', 'Accept': 'application/vnd.github+json'}
    token = os.environ.get('GH_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    with urllib.request.urlopen(urllib.request.Request('https://api.github.com' + path, headers=headers), timeout=40) as response:
        return json.load(response)

def generate():
    repos = []
    page = 1
    while True:
        batch = get(f'/users/{OWNER}/repos?per_page=100&page={page}')
        repos.extend(r for r in batch if not r['fork'] and r['name'].lower() != OWNER.lower())
        if len(batch) < 100:
            break
        page += 1
    languages = collections.Counter()
    for repo in repos:
        languages.update(get(f'/repos/{OWNER}/{repo["name"]}/languages'))
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    stats = [('PUBLIC PROJECTS', len(repos)), ('STARS', sum(r['stargazers_count'] for r in repos)), ('FORKS', sum(r['forks_count'] for r in repos))]
    body = '<text x="28" y="30" fill="#bc99aa" font-size="10" letter-spacing="2">PUBLIC WORK / REPOSITORY SNAPSHOT</text>'
    for i, (label, value) in enumerate(stats):
        x = 28 + i * 165
        body += f'<text x="{x}" y="78" fill="#edcf92" font-size="32" font-weight="600">{value}</text><text x="{x}" y="101" fill="#c4afbf" font-size="10" letter-spacing="1">{label}</text>'
    body += '<path d="M28 124H872" stroke="#513244"/><text x="28" y="150" fill="#e2cfae" font-size="12">Source composition</text>'
    total = sum(languages.values()) or 1
    top = languages.most_common(5)
    for i, (name, count) in enumerate(top):
        y = 178 + i * 27
        pct = 100 * count / total
        body += f'<text x="28" y="{y}" fill="#d2c4ce" font-size="12">{html.escape(name)}</text><rect x="190" y="{y-10}" width="560" height="8" rx="4" fill="#362333"/><rect x="190" y="{y-10}" width="{560*pct/100:.2f}" height="8" rx="4" fill="#c9a566"/><text x="825" y="{y}" text-anchor="end" fill="#edcf92" font-size="11">{pct:.1f}%</text>'
    height = 210 + len(top) * 27
    body += f'<text x="28" y="{height-22}" fill="#ac8d9f" font-size="10">GitHub language bytes, not proficiency. Updated {stamp}</text>'
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{height}" viewBox="0 0 900 {height}" role="img"><title>Public repository snapshot, updated {stamp}</title><rect width="900" height="{height}" rx="18" fill="#160f18"/><g font-family="Segoe UI,Arial,sans-serif">{body}</g></svg>'
    (ROOT / 'assets').mkdir(exist_ok=True)
    (ROOT / 'assets/activity.svg').write_text(svg, encoding='utf-8')
    print(json.dumps({'updated': stamp, 'projects': len(repos), 'languages': dict(languages)}, indent=2))

if __name__ == '__main__':
    generate()
