# File Management

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

Possibly consider running these commands:
```
mkdir mov
mkdir pic

mv *.MOV mov/
mv *.mov mov/
mv *.MP4 mov/
mv *.mp4 mov/

mv *.JPG pic/
mv *.HEIC pic/
mv *.heic pic/
mv *.PNG pic/
mv *.png pic/
mv *.jpg pic/
mv *.jpeg pic/
```

TODO:

Include rclone commands to move everything to AND from Google drive
