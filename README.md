## This is the ETL pipeline which works in 3 steps-:

` 1) -: It extract the data from sql database.
2) -: It transform the data as required.
3)-: It load the data in Postgres Sql database. `

## I have built a CI/CD pipeline in Jenkins to do so. 

## Pipeline has 4 stages as mentioned below-:

` 1) -: Gitclone -: It clone the github repository.
2) -: Build -: It build the docker image of the enivornment.
3) -: Run -: It run the code.
4) -: Push -: It push the docker image in dockerhub. `

<img width="1275" alt="ETL" src="https://github.com/user-attachments/assets/44bdd6df-b20f-4e00-b95b-e1846dcdc9fd" />

