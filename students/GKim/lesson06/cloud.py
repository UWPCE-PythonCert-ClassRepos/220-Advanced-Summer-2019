{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import boto3\n",
    "\n",
    "from botocore.exceptions import ClientError"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "region = \"us-west-2\"\n",
    "\n",
    "s3 = boto3.client(\"s3\", region_name=region)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-3-20a61ffb713f>, line 7)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-3-20a61ffb713f>\"\u001b[1;36m, line \u001b[1;32m7\u001b[0m\n\u001b[1;33m    with open(file_url.split(\"/\"))[-1], \"wb\") as file:\u001b[0m\n\u001b[1;37m                                            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import requests\n",
    "\n",
    "file_url = \"https://data.teleona.com/iris.csv\"\n",
    "\n",
    "r = request.get(file_url, allow_redirects=True)\n",
    "with open(file_url.split(\"/\"))[-1], \"wb\") as file:\n",
    "    file.write(r.content)\n",
    "    "
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
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
