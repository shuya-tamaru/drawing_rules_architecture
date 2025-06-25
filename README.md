# Drawing Rules Architecture（図面ルールアーキテクチャ）

## 概要

このリポジトリは、Rhinoceros（Rhino）を用いた建築図面作成のための標準ルール・テンプレート・ドキュメントを提供します。図面のレイヤ・線種・文字・図面枠の運用を統一し、効率的かつ高品質な図面作成をサポートします。

## ディレクトリ構成

```
drawing-rules-architecture/
├── rhino-rules/
│    ├── drawing_frame.md
│    ├── drawing_layers.md
│    ├── drawing_line.md
│    └── drawing_text.md
├── rhino_drawing_frame_templates/
│    ├── drawing_template_a3_v6.3dm
│    ├── drawing_template_a3_v7.3dm
│    └── drawing_template_a3_v8.3dm
```

## 使い方

1. **テンプレートの利用**
   - `rhino_drawing_frame_templates`フォルダから、Rhinoのバージョン（v6/v7/v8）に合わせて`.3dm`ファイルをダウンロードしてください。

2. **図面ルールの参照**
   - `rhino-rules/`フォルダ内のMarkdownファイルを参照し、各種ルールに従って作図してください。
     - `drawing_frame.md`：図面枠の管理・自動化ルール
     - `drawing_layers.md`：レイヤ命名規則・推奨レイヤ構成
     - `drawing_line.md`：線種命名規則・運用ルール
     - `drawing_text.md`：文字スタイル命名規則・運用ルール

3. **カスタマイズ**
   - 新しい文字スタイルや線種が必要な場合は、各Markdownファイルの命名規則に従って追加してください。
   - プロジェクト固有の要件がある場合も、基本ルールに沿って拡張してください。

## 各フォルダ・ファイルの説明

- **rhino-rules/**
  - 図面標準ルール（レイヤ・線種・文字・図面枠）をMarkdown形式でまとめています。
- **rhino_drawing_frame_templates/**
  - Rhino各バージョン用の図面枠テンプレート（.3dmファイル）を格納しています。
