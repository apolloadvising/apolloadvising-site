// Renders an HTML file to a Letter PDF with a running footer. Usage: node render.js in.html out.pdf "<footer html>"
const { chromium } = require('playwright');
(async () => {
  const [src, out, footer] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + src, { waitUntil: 'load' });
  await p.pdf({ path: out, format: 'Letter', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>', footerTemplate: footer || '<span></span>',
    margin: { top: '0.62in', bottom: '0.7in', left: '0.7in', right: '0.7in' } });
  await b.close();
})();
