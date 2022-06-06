'開発タブを表示
'[ファイル]→[オプション]→[リボンのユーザー設定]→[開発]

'エディタを起動
'[開発]→[Visual Basic]

'モジュールを作成
'[挿入]→[標準モジュール]

'保存
'拡張子を.xlsmにする

'プロシージャ
Sub x()
    '出力
    Debug.Print x 'イミディエイトウィンドウ

    '入力
    InputBox("x")

    '型
    x     '数値(整数)
    x.x   '数値(小数)
    "x"   '文字列
    True  '真偽値(真)
    False '真偽値(偽)

    '演算子
        '算術
        x + x   '加算
        x - x   '減算
        x * x   '乗算
        x ^ x   '冪乗
        x / x   '除算
        x \ x   '整数除算
        x Mod x '剰余
        
        '連結
        x & x

        '比較
        x = x  '等価
        x <> x '不等価
        x < x  '未満
        x <= x '以下
        x > x  '超過
        x >= x '以上

        'Like
        x Like "?"      '1文字
        x Like "#"      '1文字(数字)
        x Like "*"      '0-1文字
        x Like "[x-x]"  '範囲内の1文字
        x Like "[!x-x]" '範囲外の1文字

        '論理
        x And x '論理積
        x Or x  '論理和
        x Xor x '排他的論理和
        Not x   '論理否定

    '変数
    Dim x '宣言
    x = x '代入
    x     '呼び出し
    
    '判定
    IsNumeric(x) '数値
    IsDate(x)    '日付
    IsArray(x)   '配列
    IsError(x)   'エラー
    IsEmpty(x)   '空白


    '分岐
    If x Then
        x
    ElseIf x Then
        x
    Else
        x
    End If

    '繰り返し
        '回数
        For x = x To x Step x
            x
            Exit For
        Next

        '配列
        For Each x In x
            x
            Exit For
        Next

        '条件(～の間)
        Do While x
            x
            x = x + 1
            Exit Do
        Loop

        '条件(～まで)
        Do Until x
            x
            x = x + 1
            Exit Do
        Loop

    '配列
    x = Array(x)    '作成
    x(x)            '呼び出し
    Split("x", "x") '文字列→配列
    Join(x, "x")    '配列→文字列
End Sub