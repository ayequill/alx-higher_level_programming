#!/usr/bin/node

const fs = require('fs').promises;

async function concatFiles (file1, file2, file3) {
  try {
    const data1 = await fs.readFile(file1, 'utf8');
    const data2 = await fs.readFile(file2, 'utf8');

    await fs.writeFile(file3, data1, 'utf8');
    await fs.writeFile(file3, data2, { flag: 'a' }, 'utf8');
  } catch (e) {
    console.error(e);
  }
}

const [, , file1, file2, file3] = process.argv;

if (file1 && file2 && file3) {
  concatFiles(file1, file2, file3);
}
