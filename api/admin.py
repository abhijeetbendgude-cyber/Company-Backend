from django.contrib import admin
from api.models import Company,Employee,Project

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location','type']
    list_filter = ['type']
    search_fields = ['name','location','type']
    ordering = ['name']
    list_per_page = 10
    

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['name','email','phone','position','company']
    list_filter = ['company','position']
    search_fields = ['name','email','address','phone','position']
    ordering = ['name']
    list_per_page = 10
    list_display_links = ['name']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date', 'end_date', 'company', 'get_employees', 'status']

    def get_employees(self, obj):
        return ", ".join([e.name for e in obj.employee.all()])

    get_employees.short_description = 'Employees'  # Optional: Nice column name in admin

    
    

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Project,ProjectAdmin)
