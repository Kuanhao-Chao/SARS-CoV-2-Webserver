# from model import parameters
from model import person
from model import vaccine
from model import model

# person.Person(.value)

# vaccine.Vaccine(10.value)

p = person.Person(age = 98)

#
print("           curr status: ", p.curr_status.value)
print("                    id: ", p.id)
print("    contactperson_rate: ", p.contactperson_rate.value)
print("    seektreatment_rate: ", p.seektreatment_rate.value)
print("           curr_status: ", p.curr_status.value)
print("                   day: ", p.day)
print("                   age: ", p.age)
print("             age_group: ", p.age_group.value)
print("    youth_contact_rate: ", p.youth_contact_rate.value)
print("    adult_contact_rate: ", p.adult_contact_rate.value)
print("    elder_contact_rate: ", p.elder_contact_rate.value)
print("          vaccine_rate: ", p.vaccine_rate.value)
print("        n_vaccine_rate: ", p.n_vaccine_rate.value)
print("    vac_infection_rate: ", p.vac_infection_rate.value)
print("  vac_n_infection_rate: ", p.vac_n_infection_rate.value)
print("  n_vac_infection_rate: ", p.n_vac_infection_rate.value)
print("n_vac_n_infection_rate: ", p.n_vac_n_infection_rate.value)

# p.vaccine_status = p.set_vaccine_status(.value)

print("               smt_hospitalized_rate: ", p.smt_hospitalized_rate.value)
print("                        smt_opd_rate: ", p.smt_opd_rate.value)
print("         smt_hospitalized_death_rate: ", p.smt_hospitalized_death_rate.value)
print("      smt_hospitalized_recovery_rate: ", p.smt_hospitalized_recovery_rate.value)
print("               smt_opd_medicine_rate: ", p.smt_opd_medicine_rate.value)
print("             smt_opd_n_medicine_rate: ", p.smt_opd_n_medicine_rate.value)
print("         smt_opd_m_hospitalized_rate: ", p.smt_opd_m_hospitalized_rate.value)
print("             smt_opd_m_recovery_rate: ", p.smt_opd_m_recovery_rate.value)
print("   smt_opd_m_hospitalized_death_rate: ", p.smt_opd_m_hospitalized_death_rate.value)
print("smt_opd_m_hospitalized_recovery_rate: ", p.smt_opd_m_hospitalized_recovery_rate.value)
print("        smt_opd_nm_hospitalized_rate: ", p.smt_opd_nm_hospitalized_rate.value)
print("            smt_opd_nm_recovery_rate: ", p.smt_opd_nm_recovery_rate.value)
print(" smt_opd_nm_hospitalized_death_srate: ", p.smt_opd_nm_hospitalized_death_rate.value)
print("      smt_opd_nm_recovery_death_rate: ", p.smt_opd_nm_recovery_death_rate.value)

m = model.VaccineModel()
m.one_day_passed()
m.one_day_passed()
m.one_day_passed()
m.one_day_passed()
m.one_day_passed()
m.one_day_passed()
m.one_day_passed()
m.one_day_passed()
m.one_day_passed()
m.one_day_passed()
m.one_day_passed()

# print("         age      : ", p.age.value)
# print("         age group: ", p.age_group.value.value)
# print("      route status: ", p.route_status.value.value)
# p.choose_route(.value)
# print("route status again: ", p.route_status.value.value)
# p.choose_route(.value)
# print("route status again: ", p.route_status.value.value)
# p.choose_route(.value)
# print("route status again: ", p.route_status.value.value)
# p.choose_route(.value)
# print("route status again: ", p.route_status.value.value)
# p.choose_route(.value)
# print("route status again: ", p.route_status.value.value)
# p.choose_route(.value)
# print("route status again: ", p.route_status.value.value)
# p.choose_route(.value)
# print("route status again: ", p.route_status.value.value)
#
#
# print("youth contact rate: ", p.youth_contact_rate.value.value)
# print("adult contact rate: ", p.adult_contact_rate.value.value)
# print("elder contact rate: ", p.elder_contact_rate.value.value)
# print("      vaccine rate: ", p.vaccine_rate.value.value)
# print("    vaccine status: ", p.vaccine_status.value)
# print("    infection rate: ", p.infection_rate.value.value)
# print("  infection status: ", p.infection_status.value)
#
# # print("  medicine_48_status: ", p.medicine_48_status.value)
# print(" seek treatment rate: ", p.seek_treatment_rate.value.value)
# print("seektreatment status: ", p.seek_treatment_status.value)
# print("medicine intake rate: ", p.medicine_intake_rate.value.value)
# print("medicine intake status: ", p.medicine_intake_status.value)
# print("         severe rate: ", p.severe_rate.value.value)
# print("       severe status: ", p.severe_status.value)
# print("       fatality rate: ", p.fatality_rate.value.value)
# print("  effectiveness mild: ", p.effectiveness_mild.value.value)
# print("effectiveness severe: ", p.effectiveness_severe.value.value)
# print(" effectiveness death: ", p.effectiveness_death.value.value)
#
# md = model.VaccineModel(.value)
# print("     md idx_case_num: ", md.idx_case_num.value)
# print("          md sim_day: ", md.sim_day.value)
# print("         md sim_time: ", md.sim_time.value)
# print("       md cycle_days: ", md.cycle_days.value)
# # print("  md transmission_gp: ", md.transmission_gp.value)
# # print("     md treatment_gp: ", md.treatment_gp.value)
# # print("         md death_gp: ", md.death_gp.value)
# # print("      md recovery_gp: ", md.recovery_gp.value)
#
# md.one_day_passed(.value)
# md.one_day_passed(.value)
# md.one_day_passed(.value)
# md.one_day_passed(.value)
# md.one_day_passed(.value)
# md.one_day_passed(.value)
# md.one_day_passed(.value)
# md.one_day_passed(.value)
# md.one_day_passed(.value)
# md.one_day_passed(.value)
