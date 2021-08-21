import urllib.parse



if __name__ == '__main__':
    values =[

        {

            "code":"362329199102240018", "name":"张少宗", "cusType":"PERSONAL"

        }, {

            "code":"362329198902251642", "name":"程沈丽", "cusType":"PERSONAL"

        }

    ]
    jsonstr = str(values)
    data=urllib.parse.quote(jsonstr)
    print(data)