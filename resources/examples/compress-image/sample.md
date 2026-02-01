# 图片压缩示例

## 示例 1：基本压缩

### 输入

```
/compress-image-full
图片: https://example.com/image.jpg
质量: 80
尺寸: 1024x768
```

### 输出

```
Successfully compressed image to compressed_image.jpg
Original size: 2.5 MB
Compressed size: 780 KB
Compression ratio: 68.8%
```

## 示例 2：高质量压缩

### 输入

```
/compress-image-full
图片: https://example.com/photo.jpg
质量: 95
尺寸: 1920x1080
```

### 输出

```
Successfully compressed image to compressed_photo.jpg
Original size: 5.2 MB
Compressed size: 2.1 MB
Compression ratio: 59.6%
```

## 示例 3：快速压缩

### 输入

```
/compress-image-quick
图片: https://example.com/quick.jpg
```

### 输出

```
Successfully compressed image to compressed_quick.jpg
Original size: 1.8 MB
Compressed size: 520 KB
Compression ratio: 71.1%
```

## 示例 4：小尺寸缩略图

### 输入

```
/compress-image-full
图片: https://example.com/original.jpg
质量: 75
尺寸: 200x200
```

### 输出

```
Successfully compressed image to compressed_thumbnail.jpg
Original size: 3.1 MB
Compressed size: 45 KB
Compression ratio: 98.5%
```

## 示例 5：本地文件压缩

### 输入

```
/compress-image-full
图片: ./local-image.png
质量: 85
尺寸: 800x600
```

### 输出

```
Successfully compressed image to compressed_local.png
Original size: 1.2 MB
Compressed size: 320 KB
Compression ratio: 73.3%
```
