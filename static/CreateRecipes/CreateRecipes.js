// Go to pages
function goToHome() {
    window.location.href = '/';
}

function goToFavoriteRecipes() {
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
            window.location.href = '/FavoriteRecipes';
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

// Ingredients
const addIngredient = document.querySelector("#addIngredient");
const removeIngredient = document.querySelector("#removeIngredient");
const ingredientMenu = document.querySelector("#ingredientMenu");
let counterIngredient = 2;

function addIngredientFunc()
{
    const item = document.createElement('li');
    item.innerHTML = `
                    <label>Ingredient ${counterIngredient}:</label>
                    <textarea class="textBox" placeholder="Input ingredient"></textarea>`;

    ingredientMenu.appendChild(item);
    
    counterIngredient++;
}

function removeIngredientFunc()
{
    if (ingredientMenu.children.length > 1)
    {
        ingredientMenu.removeChild(ingredientMenu.lastElementChild);
        counterIngredient--;
    }
}

// Steps
const addStep = document.querySelector("#addStep");
const removeStep = document.querySelector("#removeStep");
const stepMenu = document.querySelector("#stepMenu");
let counterSteps = 2;

function addStepFunc()
{
    const item = document.createElement('li');
    item.innerHTML = `
                    <label>Step ${counterSteps}:</label>
                    <textarea class="textBox" placeholder="Input step"></textarea>`;

    stepMenu.appendChild(item);
    
    counterSteps++;
}

function removeStepFunc()
{
    if (stepMenu.children.length > 1)
    {
        stepMenu.removeChild(stepMenu.lastElementChild);
        counterSteps--;
    }
}

// Finish creating recipe
function clearSpreadsheet()
{
    ingredientMenu.innerHTML = `
                        <li>
                            <label>Ingredient 1:</label>
                            <textarea class="textBox" placeholder="Input ingredient"></textarea>
                        </li>`

    stepMenu.innerHTML = `
                        <li>
                            <label>Step 1:</label>
                            <textarea class="textBox" placeholder="Input step"></textarea>
                        </li>`

    const recipeName = document.querySelector('#recipeName');
    recipeName.value = "";
}

function finishCreating()
{
    // Get li elements
    const ingredientMenuLi = document.querySelectorAll('#ingredientMenu li');
    const stepMenuLi = document.querySelectorAll('#stepMenu li');
    const recipeName = document.querySelector('#recipeName');

    // Buffor arrays for ingredients and steps
    let name = []
    let ingredients = [];
    let steps = [];

    // Iterate through ul items and check does textboxes are filled or not
    let emptyIngredient = true;
    ingredientMenuLi.forEach((li) => {
        const textareaItemIngredient = li.querySelector('textarea');

        if(textareaItemIngredient.value != "")
        {
            ingredients.push(textareaItemIngredient.value);
            emptyIngredient = false;
        }
    })

    let emptySteps = true;
    stepMenuLi.forEach((li) => {
        const textareaItemStep = li.querySelector('textarea');

        if(textareaItemStep.value != "")
        {
            steps.push(textareaItemStep.value);
            emptySteps = false;
        }
    })

    let emptyRecipeName = true;
    if (recipeName.value != "")
    {
        name.push(recipeName.value);
        emptyRecipeName = false;
    }

    // Get final response does spreadsheet is valid or not
    if(!emptyIngredient && !emptySteps && !emptyRecipeName)
    {
        // Parse table to json
        fetch('/AddToFavorite', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({name, ingredients, steps})
          })
            .catch(error => {
              console.error(error);
          }); 

        alert('Your recipe has been saved!');
        clearSpreadsheet();
    }
    else if(emptyRecipeName)
    {
        alert('Your recipe has no name!')
    }
    else
    {
        alert('Spreadsheet is invalid! Full fill at least one step and one ingredient!')
    }
}