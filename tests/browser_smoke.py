# BareBones Project | Browser smoke test
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def main():
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(f"http://127.0.0.1:{server.server_port}/index.html")
            page.wait_for_timeout(250)
            assert page.locator("canvas#scene").evaluate("el => el.width > 0 && el.height > 0")
            assert page.locator(".signature").inner_text() == "BareBones Project"
            page.locator("#pause").click()
            assert page.locator("#pause").inner_text() == "RESUME"
            page.locator("#pause").click()
            assert page.locator("#pause").inner_text() == "PAUSE"
            page.locator("#speed").fill("2")
            assert page.locator("#speed").input_value() == "2"
            page.locator("#reset").click()
            assert page.locator("#speed").input_value() == "1"
            page.mouse.move(610, 320)
            page.mouse.down()
            page.mouse.move(650, 360, steps=5)
            page.mouse.up()
            page.set_viewport_size({"width": 390, "height": 844})
            page.wait_for_timeout(150)
            assert page.locator("canvas#scene").evaluate("el => el.width > 0 && el.height > 0")
            assert not errors, errors
            browser.close()
            print("PASS: visual canvas, branding, buttons, slider, drag, mobile, no JS exceptions")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
