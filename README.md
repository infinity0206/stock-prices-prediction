# stock-prices-prediction

## ビルド & コンテナ実行
```
docker-compose build
docker-compose up -d
```

## 株価データダウンロード
```
docker-compose exec app bash
python /app/downloader.py
```

## 株価予測
- トレーニングセットとか簡単に設定できるように調整中。
```
python /app/prediction.py
```

## 参考文献
- https://qiita.com/ympnov22/items/0dd0dfd1785015e8b36f
- https://qiita.com/hook125/items/9d686382cd16907f84ab