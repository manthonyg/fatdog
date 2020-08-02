async function fetchData(dogName) {
    await fetch(`https://api.thedogapi.com/v1/breeds/search?q=${dogName}`)
    .then(res => {
        return res.json()
    }).then(data => {
        return data
    })
}

