#nesting
capitals={
    "france":"paris",
    "germany":"berlin"
}

#nesting a list in a dictionary
travel_log={
"France":{"city":["Paris","Lille","Dijon"],"total_visits":10},
"france":{"city":["Paris","Lille","Dijon"],"total_visits":12},
"Germany":{"city":["berlin","Hamburg","Stuttgart"],"total_visits":5}

}
#nesting dictionary in a list

travel_log=[
{"country":"France",
"city":["Paris","Lille","Dijon"],
"total_visits":10
},
{"country":"france",
"city":["Paris","Lille","Dijon"],
"total_visits":12
},
{"country":"Germany",
"city":["berlin","Hamburg","Stuttgart"],

"total_visits":5
}

]
