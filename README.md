# File Management

These are the steps I use to get photos and videos off of my phone and move to Google Drive.

1. Connect iphone via USB
2. Open with Apple photos
3. Export all content as unmodified original to a folder
4. Follow steps below

### Remember
- Start running Docker on Desktop first


Build Docker container

Update the build argument here!
```bash
docker build -t date-adder:latest --build-arg SOURCE_DIR=/Users/tylernakamura/Desktop/src .
```

Run Docker container

Also update the first file path here

```bash
docker run -v /Users/tylernakamura/Desktop/src:/app/src date-adder:latest
```

convert the HEICs (WILL DELETE THE HEIC AFTER):
```
for file in *.HEIC; do
  sips -s format jpeg "$file" --out "${file%.*}.jpg" && rm "$file"
done
```

Possibly consider running these commands:
```
mkdir mov
mkdir pic

rm *.aae

mv *.MOV mov/
mv *.mov mov/
mv *.MP4 mov/
mv *.mp4 mov/

mv *.JPG pic/
mv *.JPEG pic/
mv *.HEIC pic/
mv *.heic pic/
mv *.PNG pic/
mv *.png pic/
mv *.jpg pic/
mv *.jpeg pic/
```



TODO:

Include rclone commands to move everything to AND from Google drive
