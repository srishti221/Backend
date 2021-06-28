from rest_framework import serializers
from ResumebApp.models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=('StudentId',
                 'FirstName',
                 'LastName',
                 'DateofBirth',
                 'Email',
                 'Phoneno',
                 'Gender',
                 'City',
                 'State',
                 'Zip',
                 'PermanentAddress',
                 'CorrespondenceAddress',
                 'Percentage10',
                 'Percentage12',
                 'YearofPassing10',
                 'YearofPassing12',
                 'College',
                 'Course',
                 'Branch',
                 'Year',
                 'Certifications',
                 'InternshiCompany',
                 'Duration',
                 'Domain',
                 'workdescription',
                 'Projectsundertaken',
                 'Skills',
                 'Workexperience',
                 'Whatareyouplanningaftergraduation',
                 'Areaofinterest')