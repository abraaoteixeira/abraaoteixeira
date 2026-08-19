from playwright.sync_api import sync_playwright
from PIL import Image
import io
import os

SVGS = [
    "dark_mode.svg",
    "light_mode.svg",
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for svg in SVGS:
        page = browser.new_page(viewport={"width": 1200, "height": 850})
        # Use absolute path to the local SVG
        file_url = f"file://{os.path.abspath(svg).replace(os.sep, '/')}"
        page.goto(file_url, wait_until="networkidle")

        frames = []
        for _ in range(30):
            page.wait_for_timeout(100)
            frames.append(page.screenshot())

        name = svg.replace(".svg", ".webp")
        images = [Image.open(io.BytesIO(f)) for f in frames]
        images[0].save(
            name,
            save_all=True,
            append_images=images[1:],
            duration=100,
            loop=0,
        )
        print(f"Saved {name}")
        page.close()

    browser.close()
