// Go to pages
function goToHome() {
    window.location.href = '/';
}

function goToCreateRecipes() {
    fetch('/Data')
    .then(response => {
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      return response.json();
    })
    .then(data => {
        let loggedUser = data.Logged;
        let loggedIn = false;

        if (loggedUser.length != 0)
        {
            loggedIn = true;
        }

        if (loggedIn)
        {
            window.location.href = '/CreateRecipes';
        }
        else
        {
            alert('Firstly you must log in!');
        }
    })
    .catch(error => {
        console.log(error);
    });
}

// Check is user logged!
const logged = document.querySelector('.logged');
const logOut = document.querySelector('#logOut');

fetch('/Data')
.then(response => {
  if (!response.ok) {
    throw new Error('Failed to fetch data');
  }
  return response.json();
})
.then(data => {
    let loggedUser = data.Logged;

    if (loggedUser.length != 0)
    {
        logged.style.display = 'block';
        logged.innerHTML = `Logged:
                            <br><br> ${loggedUser[0]}
                            <br><br>`;
        logOut.style.display = 'block';
        logOut.innerHTML = `Log out`
    }
    else
    {
        alert('You are not loged in!');
        window.location.href = '/';
    }
})
.catch(error => {
    alert('You are not loged in!');
    window.location.href = '/';
});

// Show recipe steps and ingredients
function showRecipe(name)
{
  fetch('/Data')
  .then(response => {
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    return response.json();
  })
  .then(data => {
      const listRecipes = document.querySelectorAll('#favoriteUL li');
      const listIngredients = document.querySelector('#favoriteULIngredients');
      const listSteps = document.querySelector('#favoriteULSteps');
      const hiddenBox1 = document.querySelector('.favoriteBoxHid1');
      const hiddenBox2 = document.querySelector('.favoriteBoxHid2');

      listRecipes.forEach((li) => {
        const a = li.querySelector('a');
        a.style.color = "#fff";
      });

      name.style.color = "#555";
      listIngredients.innerHTML = "";
      listSteps.innerHTML = "";

      let recipes = data.FavoriteList;
      recipes.forEach(element => {
        if(element['name'][0] == name.textContent)
        { 
          // Append ingredients
          for (let i = 0; i < element['ingredients'].length; i++)
          {
            listIngredientElement = document.createElement('li');
            listIngredientElement.innerHTML = `<a>${element['ingredients'][i]}</a>`;
        
            listIngredients.appendChild(listIngredientElement);
          }

          // Append steps
          for (let i = 0; i < element['steps'].length; i++)
          {
            listStepElement = document.createElement('li');
            listStepElement.innerHTML = `<a>${element['steps'][i]}</a>`;

            listSteps.appendChild(listStepElement);
          }
        }
      });

      hiddenBox1.style.display = 'block';
      hiddenBox2.style.display = 'block';
  })
  .catch(error => {
    console.log(error);
  });
}

// Show favorite recipes list
fetch('/Data')
.then(response => {
  if (!response.ok) {
    throw new Error('Failed to fetch data');
  }
  return response.json();
})
.then(data => {
    const empty = document.querySelector('#favoriteULempty');
    const list = document.querySelector('#favoriteUL');
    let recipes = data.FavoriteList;

    if (recipes.length != 0)
    {
      recipes.forEach(element => {
        listElement = document.createElement('li');
        let name = element['name'][0];
        
        listElement.innerHTML = `<a id="recipeButton" onclick="showRecipe(this)">${name}</a>`
        list.appendChild(listElement);
      });
    }
    else
    {
      empty.style.display = 'block';
    }
})
.catch(error => {
  console.log(error);
});

// Log out handler
logOut.addEventListener('click', (e) => {
    e.preventDefault()

    fetch('/LogOut', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json'
        },
      })
        .catch(error => {
          console.error(error);
      }); 
    
    alert('Successfully loged out!');
    window.location.href = '/';
})