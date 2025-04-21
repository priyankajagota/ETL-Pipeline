# FROM  python:3.9-bullseye

# Using the official Python image, Tag 3.8.3-buster
FROM python:3.8.3-buster

# # UPDATE APT-GET
# RUN apt-get update

# # PYODBC DEPENDENCES
# RUN apt-get install -y tdsodbc unixodbc-dev
# RUN apt install unixodbc-bin -y
# RUN apt-get clean -y
# ADD odbcinst.ini /etc/odbcinst.ini

# # UPGRADE pip3
# RUN pip3 install --upgrade pip

# # DEPENDECES FOR DOWNLOAD ODBC DRIVER
# RUN apt-get install apt-transport-https 
# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
# RUN apt-get update

# # INSTALL ODBC DRIVER
# RUN ACCEPT_EULA=Y apt-get install msodbcsql17 --assume-yes


# # CONFIGURE ENV FOR /bin/bash TO USE MSODBCSQL17
# RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile 
# RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc 
# Make a directory for our application

ADD odbcinst.ini /etc/odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev freetds-dev freetds-bin tdsodbc 
RUN apt install unixodbc-bin -y
RUN apt-get clean -y

# RUN apt-get -y install unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc 

COPY freetds.conf /etc/freetds/freetds.conf
COPY odbc.ini /etc/odbc.ini
COPY odbcinst.ini /etc/odbcinst.ini

WORKDIR /application

# RUN apt-get update && apt-get install -y unixodbc unixodbc-dev
# Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Make a directory for persisting ETL data
RUN mkdir -p /etl/data



# Copy our source code
COPY etl_pipeline_configuration.py .


# Run the ETL
CMD ["python","etl_pipeline_configuration.py"]