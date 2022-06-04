'初期設定
'@Excel
'[ファイル] → [オプション] → [リボンのユーザー設定] → [開発]

'エディタ
'@Excel
'[開発] → [Visual Basic]

'モジュール
'@エディタ
'[挿入] → [標準モジュール]

'変数
Dim 変数  '宣言
変数 = 値 '書き込み
変数      '読み込み

'ブック
Workbooks.Add                                                                                        '新規作成
Workbooks("ブック")                                                                             '読み込み
.SaveAs Filename:="ブック", Password:="読み込みパスワード", WriteResPassword:="書き込みパスワード" '新規保存
.Save                                                                                              '上書き保存

'シート
Worksheets.Add Before or After:=Worksheets("基準シート") '追加
Worksheets("シート")                                '読み込み
.Name = "シート"                                       '名前
.Move Before or After:=Worksheets("基準シート")        '移動
.Copy Before or After:=Worksheets("基準シート")        'コピー
.Delete                                                '削除

'実行
'[F5]


Sub プロシージャ()
    Range("A1")                           'セル
        .Value = "Hello World"            '    値
        .Font                             '    フォント
            .Name          = "游ゴシック" '        種類
            .Size          = 8            '        サイズ
            .ColorIndex    = 1            '        色
            .Bold          = True         '        太字
            .Italic        = True         '        斜体
            .Underline     = True         '        下線
            .Strikethrough = True         '        打ち消し線
            .Superscript   = True         '        上付き
            .Subscript     = True         '        下付き
        .Borders                          '    罫線
            .LineStyle  = xlContinuous    '        種類
            .ColorIndex = 1               '        色
        .HorizontalAlignment = xlCenter   '    水平位置
        .VerticalAlignment   = xlCenter   '    垂直位置
        .Interior                         '    背景
            .ColorIndex = 色              '        色
        .Select                           '    選択
            Selection                     '        読み込み
        .MergeCells = True                '    結合
        .Copy                             '    コピー
        .ClearContents                    '    値削除
        .Delete Shift:=xlShiftUp          '    削除
    ActiveSheet                           'シート
        .Paste                            '    ペースト
End Sub