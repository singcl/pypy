const fs = require('fs');

// fs.readSync + Buffer 自定义同步获取用户输入函数
function readSyncByfs(tips) {
  tips = tips || '> ';
  process.stdout.write(tips);
  process.stdin.pause();

  const buf = Buffer.allocUnsafe(10000);
  const response = fs.readSync(process.stdin.fd, buf, 0, 10000, 0);
  process.stdin.resume();
  return buf.toString('utf8', 0, response).trim();
}

// 同步获取输入
const input = readSyncByfs('请输入任意字符：');

process.stdout.write('The result is:' + input);
process.exit(0);
