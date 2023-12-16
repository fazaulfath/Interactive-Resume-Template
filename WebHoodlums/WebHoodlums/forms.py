from django import forms
from .models import ResumeData

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeData
        fields = ['name', 'designation', 'email', 'contact', 'locationvalue',
                  'description', 'language1', 'language2', 'language3', 'language4',
                  'Professional_Skill_1', 'skill_range1', 'Professional_Skill_2',
                  'skill_range2', 'Professional_Skill_3', 'skill_range3',
                  'Professional_Skill_4', 'skill_range4', 'Technical_Skill_1',
                  'skill_range5', 'Technical_Skill_2', 'skill_range6',
                  'Technical_Skill_3', 'skill_range7', 'Technical_Skill_4', 
                  'skill_range8', 'eduname1', 'Uni1', 'startdate', 'enddate', 
                  'edudes', 'eduname2', 'Uni2'  'startdate2', 'enddate2', 'edudes2',
                  'eduname3', 'Uni3', 'startdate3', 'enddate3', 'edudes3',
                  'Domain1', 'Description1', 'Domain2', 'Description2', 'Domain3',
                  'Description3', 'Project_Name1', 'Project_Domain1',
                  'Project_Description1', 'url1', 'Project_Name2', 'Project_Domain2',
                  'Project_Description2', 'url2', 'Project_Name3', 'Project_Domain2',
                  'Project_Description3', 'url3']