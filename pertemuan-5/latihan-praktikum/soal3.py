ukm_coding = {"Andi","Budi","Caca","Deni"}
ukm_robotik = {"Caca","Deni","Euis","Fafa"}

hanya_coding = ukm_coding - ukm_robotik
set(hanya_coding)
print("Hanya mendaftar coding :", hanya_coding)

seluruh_mahasiswa = ukm_coding | ukm_robotik
print("Seluruh mahasiwa uknik :", seluruh_mahasiswa)

andi_robotik = "Andi" in ukm_robotik
print("Apakah Andi anggota robotik?", andi_robotik)