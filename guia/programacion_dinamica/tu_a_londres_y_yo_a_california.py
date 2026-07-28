LONDRES = "londres"
CALIFORNIA = "california"
def plan_operativo(arreglo_L, arreglo_C, costo_M):
    OPT_L = [(0, "")] * len(arreglo_L)
    OPT_C = [(0, "")] * len(arreglo_C)
    OPT_L[0] = (arreglo_L[0], LONDRES)
    OPT_C[0] = (arreglo_C[0], CALIFORNIA)
    for i in range(1, len(arreglo_L)):
        costo_ayer_londres, _ = OPT_L[i - 1]
        costo_ayer_california, _ = OPT_C[i - 1]
        if arreglo_L[i] + costo_ayer_londres < arreglo_L[i] + costo_ayer_california + costo_M:
            OPT_L[i] = (arreglo_L[i] + costo_ayer_londres, LONDRES)
        else:
            OPT_L[i] = (arreglo_L[i] + costo_ayer_california + costo_M, CALIFORNIA)
        if arreglo_C[i] + costo_ayer_california < arreglo_C[i] + costo_ayer_londres + costo_M:
            OPT_C[i] = (arreglo_C[i] + costo_ayer_california, CALIFORNIA)
        else:
            OPT_C[i] = (arreglo_C[i] + costo_ayer_londres + costo_M, LONDRES)
    return reconstruccion(OPT_L, OPT_C)


def reconstruccion(OPT_L, OPT_C):
    res = []
    if OPT_C[-1][0] <= OPT_L[- 1][0]:
		ciudad = CALIFORNIA
    else:
		ciudad = LONDRES

	for i in range(len(OPT_C), 0, -1):
		res.append(ciudad)
		if ciudad == CALIFORNIA:
			ciudad = OPT_C[i-1][1]
		else:
			ciudad = OPT_L[i-1][1]

	res.reverse()
	return res
