const { chromium } = require('playwright-core');
const fs = require('fs');
const path = require('path');

const DIR = __dirname;
const EXEC = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

(async () => {
  const browser = await chromium.launch({
    executablePath: EXEC,
    headless: true,
    args: ['--no-sandbox', '--force-color-profile=srgb', '--hide-scrollbars']
  });
  const page = await browser.newPage({
    viewport: { width: 1080, height: 1440 },
    deviceScaleFactor: 1
  });

  const files = fs.readdirSync(DIR)
    .filter(f => /^[ab]\d\d\.html$/.test(f))
    .sort();

  let ok = 0;
  for (const f of files) {
    const png = path.join(DIR, f.replace('.html', '.png'));
    await page.goto('file://' + path.join(DIR, f), { waitUntil: 'networkidle' });
    await page.screenshot({ path: png, clip: { x:0, y:0, width:1080, height:1440 } });
    ok++;
  }
  await browser.close();
  console.log('Screenshot done:', ok, 'png files');
})().catch(e => { console.error('ERR', e); process.exit(1); });
