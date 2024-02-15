import aiohttp

async def get_data():
    kode_wilayah = [
        [11, 'Aceh'], [51, 'Bali'], [36, 'Banten'], [17, 'Bengkulu'],
        [34, 'Daerah Istimewa Yogyakarta'], [31, 'DKI Jakarta'], [75, 'Gorontalo'],
        [15, 'Jambi'], [32, 'Jawa Barat'], [33, 'Jawa Tengah'], [35, 'Jawa Timur'],
        [61, 'Kalimantan Barat'], [63, 'Kalimantan Selatan'], [62, 'Kalimantan Tengah'],
        [64, 'Kalimantan Timur'], [65, 'Kalimantan Utara'], [19, 'Kepulauan Bangka Belitung'],
        [21, 'Kepulauan Riau'], [18, 'Lampung'], [81, 'Maluku'], [82, 'Maluku Utara'],
        [52, 'Nusa Tenggara Barat'], [53, 'Nusa Tenggara Timur'], [91, 'Papua'],
        [92, 'Papua Barat'], [96, 'Papua Barat Daya'], [95, 'Papua Pegunungan'],
        [93, 'Papua Selatan'], [94, 'Papua Tengah'], [14, 'Riau'], [76, 'Sulawesi Barat'],
        [73, 'Sulawesi Selatan'], [72, 'Sulawesi Tengah'], [74, 'Sulawesi Tenggara'],
        [71, 'Sulawesi Utara'], [13, 'Sumatera Barat'], [16, 'Sumatera Selatan'],
        [12, 'Sumatera Utara'], [99, 'Luar Negeri']
    ]
    
    async with aiohttp.ClientSession() as session:
        async with session.get('https://sirekap-obj-data.kpu.go.id/pemilu/hhcw/ppwp.json') as response:
            if response.status != 200:
                return None
            
            obj = await response.json()
            last_updated = obj['ts']
            paslon_1 = obj['chart'].get('100025')
            paslon_2 = obj['chart'].get('100026')
            paslon_3 = obj['chart'].get('100027')
            percentage = obj['chart'].get('persen')
            tps_total = obj['progres']['total']
            tps_done = obj['progres']['progres']
                        
            if tps_total and tps_done:
                    tps_percentage = (float(tps_done) / float(tps_total)) * 100
                    tps_percentage = f"{tps_percentage:.2f}%"
            else:
                tps_percentage = "0.00%"


            wilayah_data = []
            
            for kode, data in obj['table'].items():
                wilayah_name = None
                for wilayah_kode, name in kode_wilayah:
                    if int(kode) == wilayah_kode:
                        wilayah_name = name
                        break
                if wilayah_name:
                    wilayah_data.append({
                        'wilayah': wilayah_name,
                        'paslon_1': data.get('100025'),
                        'paslon_2': data.get('100026'),
                        'paslon_3': data.get('100027'),
                        'percentage': data.get('persen'),
                        'status_progress': data.get('status_progress', False)
                    })
            
            return {
                'last_updated': last_updated + " WIB",
                'paslon_1': paslon_1,
                'paslon_2': paslon_2,
                'paslon_3': paslon_3,
                'percentage': percentage,
                'wilayah_data': wilayah_data,
                'progress': {
                    'total': tps_total,
                    'done': tps_done,
                    'percentage': tps_percentage
                }
            }