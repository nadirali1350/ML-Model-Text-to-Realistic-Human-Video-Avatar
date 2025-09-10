from fastapi import UploadFile


async def save_upload_file(upload_file: UploadFile, destination_path: str) -> None:
	with open(destination_path, "wb") as out_file:
		while True:
			chunk = await upload_file.read(1024 * 1024)
			if not chunk:
				break
			out_file.write(chunk)
