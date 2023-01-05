{

	"cells": [

	{

	"cell_type": "code",

	"execution_count": 1,

	"metadata": {},

	"outputs": [],

	"source": [

	"import pandas as pd"

	]

	},

	{

	"cell_type": "code",

	"execution_count": 2,

	"metadata": {},

	"outputs": [],

	"source": [

	"# 1. Create a DataFrame for the 201908-citibike-tripdata data. \n",

	"clean_citibike_df = pd.read_csv(\"201908-citibike-tripdata.csv\")"

	]

	},

	{

	"cell_type": "code",

	"execution_count": 3,

	"metadata": {},

	"outputs": [

	{

	"data": {

	"text/html": [

	"<div>\n",

	"<style scoped>\n",

	" .dataframe tbody tr th:only-of-type {\n",

	" vertical-align: middle;\n",

	" }\n",

	"\n",

	" .dataframe tbody tr th {\n",

	" vertical-align: top;\n",

	" }\n",

	"\n",

	" .dataframe thead th {\n",

	" text-align: right;\n",

	" }\n",

	"</style>\n",

	"<table border=\"1\" class=\"dataframe\">\n",

	" <thead>\n",

	" <tr style=\"text-align: right;\">\n",

	" <th></th>\n",

	" <th>tripduration</th>\n",

	" <th>starttime</th>\n",

	" <th>stoptime</th>\n",

	" <th>start station id</th>\n",

	" <th>start station name</th>\n",

	" <th>start station latitude</th>\n",

	" <th>start station longitude</th>\n",

	" <th>end station id</th>\n",

	" <th>end station name</th>\n",

	" <th>end station latitude</th>\n",

	" <th>end station longitude</th>\n",

	" <th>bikeid</th>\n",

	" <th>usertype</th>\n",

	" <th>birth year</th>\n",

	" <th>gender</th>\n",

	" </tr>\n",

	" </thead>\n",

	" <tbody>\n",

	" <tr>\n",

	" <th>0</th>\n",

	" <td>393</td>\n",

	" <td>2019-08-01 00:00:01.4680</td>\n",

	" <td>2019-08-01 00:06:35.3780</td>\n",

	" <td>531.0</td>\n",

	" <td>Forsyth St &amp; Broome St</td>\n",

	" <td>40.718939</td>\n",

	" <td>-73.992663</td>\n",

	" <td>408.0</td>\n",

	" <td>Market St &amp; Cherry St</td>\n",

	" <td>40.710762</td>\n",

	" <td>-73.994004</td>\n",

	" <td>35305</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1996</td>\n",

	" <td>2</td>\n",

	" </tr>\n",

	" <tr>\n",

	" <th>1</th>\n",

	" <td>627</td>\n",

	" <td>2019-08-01 00:00:01.9290</td>\n",

	" <td>2019-08-01 00:10:29.7840</td>\n",

	" <td>274.0</td>\n",

	" <td>Lafayette Ave &amp; Fort Greene Pl</td>\n",

	" <td>40.686919</td>\n",

	" <td>-73.976682</td>\n",

	" <td>3409.0</td>\n",

	" <td>Bergen St &amp; Smith St</td>\n",

	" <td>40.686744</td>\n",

	" <td>-73.990632</td>\n",

	" <td>38822</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1998</td>\n",

	" <td>2</td>\n",

	" </tr>\n",

	" <tr>\n",

	" <th>2</th>\n",

	" <td>1132</td>\n",

	" <td>2019-08-01 00:00:04.0480</td>\n",

	" <td>2019-08-01 00:18:56.1650</td>\n",

	" <td>2000.0</td>\n",

	" <td>Front St &amp; Washington St</td>\n",

	" <td>40.702551</td>\n",

	" <td>-73.989402</td>\n",

	" <td>3388.0</td>\n",

	" <td>President St &amp; Henry St</td>\n",

	" <td>40.682800</td>\n",

	" <td>-73.999904</td>\n",

	" <td>18373</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1988</td>\n",

	" <td>1</td>\n",

	" </tr>\n",

	" <tr>\n",

	" <th>3</th>\n",

	" <td>1780</td>\n",

	" <td>2019-08-01 00:00:04.1630</td>\n",

	" <td>2019-08-01 00:29:44.7940</td>\n",

	" <td>479.0</td>\n",

	" <td>9 Ave &amp; W 45 St</td>\n",

	" <td>40.760193</td>\n",

	" <td>-73.991255</td>\n",

	" <td>473.0</td>\n",

	" <td>Rivington St &amp; Chrystie St</td>\n",

	" <td>40.721101</td>\n",

	" <td>-73.991925</td>\n",

	" <td>25002</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1988</td>\n",

	" <td>1</td>\n",

	" </tr>\n",

	" <tr>\n",

	" <th>4</th>\n",

	" <td>1517</td>\n",

	" <td>2019-08-01 00:00:05.4580</td>\n",

	" <td>2019-08-01 00:25:23.4550</td>\n",

	" <td>3312.0</td>\n",

	" <td>1 Ave &amp; E 94 St</td>\n",

	" <td>40.781721</td>\n",

	" <td>-73.945940</td>\n",

	" <td>3312.0</td>\n",

	" <td>1 Ave &amp; E 94 St</td>\n",

	" <td>40.781721</td>\n",

	" <td>-73.945940</td>\n",

	" <td>31198</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1965</td>\n",

	" <td>2</td>\n",

	" </tr>\n",

	" </tbody>\n",

	"</table>\n",

	"</div>"

	],

	"text/plain": [

	" tripduration starttime stoptime \\\n",

	"0 393 2019-08-01 00:00:01.4680 2019-08-01 00:06:35.3780 \n",

	"1 627 2019-08-01 00:00:01.9290 2019-08-01 00:10:29.7840 \n",

	"2 1132 2019-08-01 00:00:04.0480 2019-08-01 00:18:56.1650 \n",

	"3 1780 2019-08-01 00:00:04.1630 2019-08-01 00:29:44.7940 \n",

	"4 1517 2019-08-01 00:00:05.4580 2019-08-01 00:25:23.4550 \n",

	"\n",

	" start station id start station name start station latitude \\\n",

	"0 531.0 Forsyth St & Broome St 40.718939 \n",

	"1 274.0 Lafayette Ave & Fort Greene Pl 40.686919 \n",

	"2 2000.0 Front St & Washington St 40.702551 \n",

	"3 479.0 9 Ave & W 45 St 40.760193 \n",

	"4 3312.0 1 Ave & E 94 St 40.781721 \n",

	"\n",

	" start station longitude end station id end station name \\\n",

	"0 -73.992663 408.0 Market St & Cherry St \n",

	"1 -73.976682 3409.0 Bergen St & Smith St \n",

	"2 -73.989402 3388.0 President St & Henry St \n",

	"3 -73.991255 473.0 Rivington St & Chrystie St \n",

	"4 -73.945940 3312.0 1 Ave & E 94 St \n",

	"\n",

	" end station latitude end station longitude bikeid usertype \\\n",

	"0 40.710762 -73.994004 35305 Subscriber \n",

	"1 40.686744 -73.990632 38822 Subscriber \n",

	"2 40.682800 -73.999904 18373 Subscriber \n",

	"3 40.721101 -73.991925 25002 Subscriber \n",

	"4 40.781721 -73.945940 31198 Subscriber \n",

	"\n",

	" birth year gender \n",

	"0 1996 2 \n",

	"1 1998 2 \n",

	"2 1988 1 \n",

	"3 1988 1 \n",

	"4 1965 2 "

	]

	},

	"execution_count": 3,

	"metadata": {},

	"output_type": "execute_result"

	}

	],

	"source": [

	"clean_citibike_df.head()"

	]

	},

	{

	"cell_type": "code",

	"execution_count": 4,

	"metadata": {},

	"outputs": [

	{

	"data": {

	"text/plain": [

	"tripduration int64\n",

	"starttime object\n",

	"stoptime object\n",

	"start station id float64\n",

	"start station name object\n",

	"start station latitude float64\n",

	"start station longitude float64\n",

	"end station id float64\n",

	"end station name object\n",

	"end station latitude float64\n",

	"end station longitude float64\n",

	"bikeid int64\n",

	"usertype object\n",

	"birth year int64\n",

	"gender int64\n",

	"dtype: object"

	]

	},

	"execution_count": 4,

	"metadata": {},

	"output_type": "execute_result"

	}

	],

	"source": [

	"# 2. Check the datatypes of your columns. \n",

	"clean_citibike_df.dtypes"

	]

	},

	{

	"cell_type": "code",

	"execution_count": 5,

	"metadata": {},

	"outputs": [],

	"source": [

	"# 3. Convert the 'tripduration' column to datetime datatype.\n",

	"clean_citibike_df[\"tripduration\"] = pd.to_datetime(clean_citibike_df[\"tripduration\"], unit = \"s\")"

	]

	},

	{

	"cell_type": "code",

	"execution_count": 6,

	"metadata": {},

	"outputs": [

	{

	"data": {

	"text/html": [

	"<div>\n",

	"<style scoped>\n",

	" .dataframe tbody tr th:only-of-type {\n",

	" vertical-align: middle;\n",

	" }\n",

	"\n",

	" .dataframe tbody tr th {\n",

	" vertical-align: top;\n",

	" }\n",

	"\n",

	" .dataframe thead th {\n",

	" text-align: right;\n",

	" }\n",

	"</style>\n",

	"<table border=\"1\" class=\"dataframe\">\n",

	" <thead>\n",

	" <tr style=\"text-align: right;\">\n",

	" <th></th>\n",

	" <th>tripduration</th>\n",

	" <th>starttime</th>\n",

	" <th>stoptime</th>\n",

	" <th>start station id</th>\n",

	" <th>start station name</th>\n",

	" <th>start station latitude</th>\n",

	" <th>start station longitude</th>\n",

	" <th>end station id</th>\n",

	" <th>end station name</th>\n",

	" <th>end station latitude</th>\n",

	" <th>end station longitude</th>\n",

	" <th>bikeid</th>\n",

	" <th>usertype</th>\n",

	" <th>birth year</th>\n",

	" <th>gender</th>\n",

	" </tr>\n",

	" </thead>\n",

	" <tbody>\n",

	" <tr>\n",

	" <th>0</th>\n",

	" <td>1970-01-01 00:06:33</td>\n",

	" <td>2019-08-01 00:00:01.4680</td>\n",

	" <td>2019-08-01 00:06:35.3780</td>\n",

	" <td>531.0</td>\n",

	" <td>Forsyth St &amp; Broome St</td>\n",

	" <td>40.718939</td>\n",

	" <td>-73.992663</td>\n",

	" <td>408.0</td>\n",

	" <td>Market St &amp; Cherry St</td>\n",

	" <td>40.710762</td>\n",

	" <td>-73.994004</td>\n",

	" <td>35305</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1996</td>\n",

	" <td>2</td>\n",

	" </tr>\n",

	" <tr>\n",

	" <th>1</th>\n",

	" <td>1970-01-01 00:10:27</td>\n",

	" <td>2019-08-01 00:00:01.9290</td>\n",

	" <td>2019-08-01 00:10:29.7840</td>\n",

	" <td>274.0</td>\n",

	" <td>Lafayette Ave &amp; Fort Greene Pl</td>\n",

	" <td>40.686919</td>\n",

	" <td>-73.976682</td>\n",

	" <td>3409.0</td>\n",

	" <td>Bergen St &amp; Smith St</td>\n",

	" <td>40.686744</td>\n",

	" <td>-73.990632</td>\n",

	" <td>38822</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1998</td>\n",

	" <td>2</td>\n",

	" </tr>\n",

	" <tr>\n",

	" <th>2</th>\n",

	" <td>1970-01-01 00:18:52</td>\n",

	" <td>2019-08-01 00:00:04.0480</td>\n",

	" <td>2019-08-01 00:18:56.1650</td>\n",

	" <td>2000.0</td>\n",

	" <td>Front St &amp; Washington St</td>\n",

	" <td>40.702551</td>\n",

	" <td>-73.989402</td>\n",

	" <td>3388.0</td>\n",

	" <td>President St &amp; Henry St</td>\n",

	" <td>40.682800</td>\n",

	" <td>-73.999904</td>\n",

	" <td>18373</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1988</td>\n",

	" <td>1</td>\n",

	" </tr>\n",

	" <tr>\n",

	" <th>3</th>\n",

	" <td>1970-01-01 00:29:40</td>\n",

	" <td>2019-08-01 00:00:04.1630</td>\n",

	" <td>2019-08-01 00:29:44.7940</td>\n",

	" <td>479.0</td>\n",

	" <td>9 Ave &amp; W 45 St</td>\n",

	" <td>40.760193</td>\n",

	" <td>-73.991255</td>\n",

	" <td>473.0</td>\n",

	" <td>Rivington St &amp; Chrystie St</td>\n",

	" <td>40.721101</td>\n",

	" <td>-73.991925</td>\n",

	" <td>25002</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1988</td>\n",

	" <td>1</td>\n",

	" </tr>\n",

	" <tr>\n",

	" <th>4</th>\n",

	" <td>1970-01-01 00:25:17</td>\n",

	" <td>2019-08-01 00:00:05.4580</td>\n",

	" <td>2019-08-01 00:25:23.4550</td>\n",

	" <td>3312.0</td>\n",

	" <td>1 Ave &amp; E 94 St</td>\n",

	" <td>40.781721</td>\n",

	" <td>-73.945940</td>\n",

	" <td>3312.0</td>\n",

	" <td>1 Ave &amp; E 94 St</td>\n",

	" <td>40.781721</td>\n",

	" <td>-73.945940</td>\n",

	" <td>31198</td>\n",

	" <td>Subscriber</td>\n",

	" <td>1965</td>\n",

	" <td>2</td>\n",

	" </tr>\n",

	" </tbody>\n",

	"</table>\n",

	"</div>"

	],

	"text/plain": [

	" tripduration starttime stoptime \\\n",

	"0 1970-01-01 00:06:33 2019-08-01 00:00:01.4680 2019-08-01 00:06:35.3780 \n",

	"1 1970-01-01 00:10:27 2019-08-01 00:00:01.9290 2019-08-01 00:10:29.7840 \n",

	"2 1970-01-01 00:18:52 2019-08-01 00:00:04.0480 2019-08-01 00:18:56.1650 \n",

	"3 1970-01-01 00:29:40 2019-08-01 00:00:04.1630 2019-08-01 00:29:44.7940 \n",

	"4 1970-01-01 00:25:17 2019-08-01 00:00:05.4580 2019-08-01 00:25:23.4550 \n",

	"\n",

	" start station id start station name start station latitude \\\n",

	"0 531.0 Forsyth St & Broome St 40.718939 \n",

	"1 274.0 Lafayette Ave & Fort Greene Pl 40.686919 \n",

	"2 2000.0 Front St & Washington St 40.702551 \n",

	"3 479.0 9 Ave & W 45 St 40.760193 \n",

	"4 3312.0 1 Ave & E 94 St 40.781721 \n",

	"\n",

	" start station longitude end station id end station name \\\n",

	"0 -73.992663 408.0 Market St & Cherry St \n",

	"1 -73.976682 3409.0 Bergen St & Smith St \n",

	"2 -73.989402 3388.0 President St & Henry St \n",

	"3 -73.991255 473.0 Rivington St & Chrystie St \n",

	"4 -73.945940 3312.0 1 Ave & E 94 St \n",

	"\n",

	" end station latitude end station longitude bikeid usertype \\\n",

	"0 40.710762 -73.994004 35305 Subscriber \n",

	"1 40.686744 -73.990632 38822 Subscriber \n",

	"2 40.682800 -73.999904 18373 Subscriber \n",

	"3 40.721101 -73.991925 25002 Subscriber \n",

	"4 40.781721 -73.945940 31198 Subscriber \n",

	"\n",

	" birth year gender \n",

	"0 1996 2 \n",

	"1 1998 2 \n",

	"2 1988 1 \n",

	"3 1988 1 \n",

	"4 1965 2 "

	]

	},

	"execution_count": 6,

	"metadata": {},

	"output_type": "execute_result"

	}

	],

	"source": [

	"clean_citibike_df.head()"

	]

	},

	{

	"cell_type": "code",

	"execution_count": 7,

	"metadata": {},

	"outputs": [

	{

	"data": {

	"text/plain": [

	"tripduration datetime64[ns]\n",

	"starttime object\n",

	"stoptime object\n",

	"start station id float64\n",

	"start station name object\n",

	"start station latitude float64\n",

	"start station longitude float64\n",

	"end station id float64\n",

	"end station name object\n",

	"end station latitude float64\n",

	"end station longitude float64\n",

	"bikeid int64\n",

	"usertype object\n",

	"birth year int64\n",

	"gender int64\n",

	"dtype: object"

	]

	},

	"execution_count": 7,

	"metadata": {},

	"output_type": "execute_result"

	}

	],

	"source": [

	"# 4. Check the datatypes of your columns. \n",

	"clean_citibike_df.dtypes"

	]

	},

	{

	"cell_type": "code",

	"execution_count": 8,

	"metadata": {},

	"outputs": [],

	"source": [

	"# 5. Export the Dataframe as a new CSV file without the index.\n",

	"clean_citibike_df.to_csv(\"cleaned-citibike-tripdata.csv\", index = False)"

	]

	},

	{

	"cell_type": "code",

	"execution_count": null,

	"metadata": {},

	"outputs": [],

	"source": []

	}

	],

	"metadata": {

	"kernelspec": {

	"display_name": "PythonData",

	"language": "python",

	"name": "pythondata"

	},

	"language_info": {

	"codemirror_mode": {

	"name": "ipython",

	"version": 3

	},

	"file_extension": ".py",

	"mimetype": "text/x-python",

	"name": "python",

	"nbconvert_exporter": "python",

	"pygments_lexer": "ipython3",

	"version": "3.7.9"

	}

	},

	"nbformat": 4,

	"nbformat_minor": 4

	}



