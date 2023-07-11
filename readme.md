
# Django Bio

## Installation after cloning the repository

1. Setup virtual environment (optional)
2. Install dependencies:
```bash
npm install
python -m pip install -r src/requirements.txt
```
3.
apply migrations to sqlite db
```bash
python src/manage.py migrate
```
4 add Social medias
sadly i did not get commands to work. a workaround is to copy the contents of `src\addSocialPlatformsToDB.py`, run `python manage.py shell` and paste in the code
``````
## Run development server:

To start the development server, use the following command:

```bash
npm run dev
```
