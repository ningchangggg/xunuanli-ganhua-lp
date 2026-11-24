import asyncio,os,sys
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(channel='chrome')
        pg=await b.new_page(viewport={'width':432,'height':900},device_scale_factor=2.5)
        await pg.goto('file://'+D+'/page.html'); await pg.wait_for_timeout(800); await pg.evaluate('document.fonts.ready')
        await pg.evaluate("document.getAnimations().forEach(a=>{a.pause();a.currentTime=600})")
        os.makedirs(D+'/sec',exist_ok=True)
        for i in sys.argv[1:]:
            await pg.locator('#'+i).screenshot(path=f'{D}/sec/{i}.png')
            bb=await pg.locator('#'+i).bounding_box(); print(i,bb)
        await b.close()
asyncio.run(main())
