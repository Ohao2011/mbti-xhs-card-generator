# MBTI 小红书内容卡生成器（零积分 CSS 出图）

纯本地、零付费 API，把 MBTI 文案一键变成小红书标准 3:4（1080×1440）图文卡片。

## 效果
- **新中式视觉**：宣纸渐变底 + 鎏金标题 + 朱红方印 + 「道」字水印
- 每张卡片页头带大标题，正文逐条排布，画布靠内容顶对齐 + 序号水印撑满
- **不依赖任何付费出图 API**（如 ImageGen），纯 HTML/CSS + 系统 Chrome 截图，成本为零

## 环境
- Python 3（仅标准库）
- Node.js + `playwright-core`
- 系统已装 Google Chrome（脚本默认路径 `/Applications/Google Chrome.app`）

## 用法
```bash
# 1) 生成单卡 HTML（输出 a01~a03.html、b01~b03.html、长页预览.html）
python3 gen_mbti.py

# 2) 用 Chrome 截图成 PNG（输出同名 .png）
node shot_mbti.js
```

## 文件结构
```
mbti-xhs-card-generator/
├── gen_mbti.py       # 文案 → 单卡 HTML（含全部 CSS 与 MBTI 文案变量）
├── shot_mbti.js      # 单卡 HTML → 1080×1440 PNG（调用系统 Chrome）
├── 长页预览.html      # 本地预览页
├── examples/         # 生成好的示例卡片 PNG（A 组 INFJ / B 组 认知功能）
└── README.md
```

## 自定义
- 改 `gen_mbti.py` 里的 `INFJ_TRUTHS` / `FUNCS` 等文案变量，即可换成你自己的内容
- 改文件顶部的 `CSS` 常量，可调视觉（配色、印章、水印）
- 卡片落款为「哦好MBTI」，可在 `main()` 中的 `foot` 参数修改

## License
MIT — 可商用、可修改，注明出处即可。
