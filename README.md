# bioinformatics-project

### Start project locally:

#### Setup API:
Navigate, create virual environment, install requirements:
```
cd api
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Run Flask API:
Change dir to api:
```bash
cd api
```

Make sure virtualenv is activated:
```bash
source venv/bin/activate
```
Then, start API by running
```bash
python app.py
```

API should now be running at `localhost:8080`


#### Start APP:
```bash
cd app/pssp
npm install
npm start
```

#### Start Pviz Page

To start the service which visualized secondary structure:

```bash
cd app/pssp/src/pviz
python3 -m http.server 3001
```