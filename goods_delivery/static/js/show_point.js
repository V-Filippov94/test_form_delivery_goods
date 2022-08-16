let btn_delivery = document.getElementById('btn_delivery')
let list_table = table.children
flag = 0
id_date_delivery.type = 'date'
id_date_delivery.style.width = '51.5%'
function show_point(){
    for(point=0; point<list_table.length; point++){
        if(list_table[point].tagName == 'TBODY'){
            flag ++
            let new_tr = document.createElement('tr')
            list_table[point].appendChild(new_tr)

            let new_td = document.createElement('td')
            new_tr.appendChild(new_td)

            let input_address_set_product = document.createElement('input')
            input_address_set_product.type = 'hidden'
            input_address_set_product.name = 'addressissuance_set-'+ flag +'-product'
            input_address_set_product.id = 'id_addressissuance_set-'+ flag +'-product'
            new_td.appendChild(input_address_set_product)

            let input_address_set = document.createElement('input')
            input_address_set.type = 'hidden'
            input_address_set.name = 'addressissuance_set-' + flag + '-id'
            input_address_set.id = 'id_addressissuance_set-' + flag + '-id'
            new_td.appendChild(input_address_set)

            let textarea_addressissuance_set = document.createElement('textarea')
            textarea_addressissuance_set.name = 'addressissuance_set-' + flag + '-address'
            textarea_addressissuance_set.cols = '40'
            textarea_addressissuance_set.rows = '10'
            textarea_addressissuance_set.id = 'id_addressissuance_set-' + flag + '-address'
            new_td.appendChild(textarea_addressissuance_set)

        }
    }
}

btn_delivery.addEventListener('click', function(e){
    show_point()
})