# BC2ODPT: BlockChain-based Certification of Open Data for Public Transportation
BC2ODPTはブロックチェーン(BC)に公共交通オープンデータ(ODPT)の
リアルタイムAPIから得られるデータを保存していくことで，その存在
を証明するアプリケーションです。

# 実行環境
- Python 3.6.5
- 必要モジュール: `requirements.txt` に記載


# アプリケーションの説明



# 実行方法
## 各ディレクトリ説明
中身コアノードとしての役割をnodeA、参加コアノードとしてnodeB、APIデータを取得し送信する役割としてclientAという３つのnodeをディレクトリごとに設定しています。  
ノードを増やしたい場合、ディレクトリごとコピーし、各node*/server2.py・client*/client_*.pyにて、接続先IP・PORTの設定をすることでノードを増やすことが可能です。

## 簡単な実行
`nodeA/server1.py`を実行することで、中身コアノードが立ち上がります。このとき、`ServerCore({PORT})`内にて起動ホストPORTを設定します。  
  
`clientA/client_while.py`を実行することで、テストデータを起動し続けるかぎり接続先サーバーに送信し続けます。接続先の設定を`ClientCore({ホストport}, '{接続先IP}', {接続先PORT})`にて行います。  
  
中心コアノードの接続先IPが分からない場合、`nodeA/server1.py`を実行することで、2行目に  
`Server IP address is set to ...  {実行プログラムのIP}`
と、起動したサーバーのIPが表示されるため、それを入力することで接続をすることができます。  
  
新規接続のサーバーnodeとしてnodeBを起動する場合、`nodeB/server2.py`を実行します。こちらの接続設定も、clientと同様に、`ServerCore({ホストport}, '{接続先IP}', {接続先PORT})`と設定を行います。  
その後、`DB2Memory Valid Check OK !!!!`というメッセージが出力されば、ブロックチェーンの同期が完了します。もしnodeBディレクトリ内の`db/ldb/`に共有されたはずのデータが無い場合、nodeBを再起動することで正常に動き直す場合があります。  
