T_SEMANA = 100
T_DIA = 42


def func_total_parking(dias):
    num_semanas = dias // 7
    num_dias = dias % 7
    return(num_semanas * T_SEMANA + num_dias * T_DIA)


total = func_total_parking(35)
print(total)