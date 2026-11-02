<template>
  <div class="p-4 text-center">
    <h1 class=" md:text-2xl xl:text-4xl font-bold dark:text-white">2048 Solo</h1>
    <h3 v-if="is_initiated===false" class="md:text-xl font-bold dark:text-white">Faites un mouvement pour commencer !</h3>
    <h3 v-else class="xl:text-xl font-bold dark:text-white">Le jeu peut se mettre en pause avec Echap</h3>
    <p v-if="backend_status.valueOf()==='down'" class="mt-2 text-gray-700">Impossible de lancer la partie</p>
  </div>

  <div class="flex flex-col-reverse  lg:flex-row">
    <div class="lg:w-1/3 flex flex-col bg-white dark:bg-gray-900">
      <div class="flex justify-center sm:text-lg md:text-xl lg:text-2xl dark:text-white mt-2 xl:mt-5">
        <p>Leaderboard</p>
      </div>
      <Leaderboard class="flex justify-around mt-5 mx-10" :leaderboard="current_leaderboard"/>
    </div>

    <div class="relative lg:w-1/3">
      <div class="bg-white dark:bg-gray-900">
        <div class="mt-1 xl:mt-4"
           :class="{'opacity-20':is_paused.valueOf()||(game_won.valueOf()&&!game_continue_after_won.valueOf())||game_lose.valueOf()}"
        >
          <GameGrid v-if="backend_status.valueOf()==='ready'" :grid="game_grid"/>
        </div>
      </div>

      <!-- Pause section, appears when the player pause the game by clicking on <Escape> -->
      <div v-if="is_paused.valueOf()" class="absolute flex flex-col justify-center items-center inset-0">
          <button type="button" @click="game_resume" class="bg-1024 text-white rounded-xl text-md px-4 py-2.5
          hover:cursor-pointer hover:bg-4096">
            Reprendre
          </button>
          <button type="button" @click="game_reset" class="bg-1024 text-white rounded-xl text-md px-4 py-2.5 mt-2
          hover:cursor-pointer hover:bg-4096">
            Quitter
          </button>
      </div>

      <!-- Won section, appears when the player win the game -->
      <div v-if="game_won.valueOf()&&!game_continue_after_won.valueOf()" class="absolute flex flex-col justify-center items-center text-center inset-0 -mt-4">
        <p class="sm:text-lg md:text-xl lg:text-3xl dark:text-white font-bold">Félicitations !</p>
        <button type="button" @click="game_continue" class="bg-1024 text-white rounded-xl text-md px-4 py-2.5 mt-3
          hover:cursor-pointer hover:bg-4096">
            Continuer à jouer
        </button>
        <button type="button" @click="game_reset" class="bg-1024 text-white rounded-xl text-md px-4 py-2.5 mt-3
          hover:cursor-pointer hover:bg-4096">
            Relancer
        </button>
      </div>

      <!-- Lose section, appears when the player lose the game -->
      <div v-if="game_lose.valueOf()" class="absolute flex flex-col justify-center items-center text-center inset-0 -mt-4">
        <p class="sm:text-lg md:text-xl lg:text-3xl dark:text-white font-bold">Dommage, vous avez perdu...</p>

        <input type="text" placeholder="Pseudonyme" v-model="player_pseudo" class="rounded-xl mt-5 opacity-90 placeholder:text-2"/>
        <button type="button" @click="save_score" class="bg-1024 text-white rounded-xl text-md px-4 py-2.5 mt-3
          hover:cursor-pointer hover:bg-4096">
            Enregistrer le score
        </button>

        <button type="button" @click="game_reset" class="bg-1024 text-white rounded-xl text-md px-4 py-2.5 mt-3
          hover:cursor-pointer hover:bg-4096">
            Relancer
        </button>
      </div>
    </div>

    <div class="flex flex-col items-center text-black bg-white dark:bg-gray-900 dark:text-white lg:w-1/3 xl:mt-5">
      <span class="sm:text-lg md:text-xl lg:text-2xl">Score</span>
      <span class="sm:text-lg md:text-xl lg:text-2xl xl:text-3xl xl:mt-5">{{game_score.valueOf()}}</span>
    </div>
  </div>

  <BackgroundEffect amount-decoration="50" duration="10"/>
</template>

<script setup>
import {ref, onMounted, onUnmounted} from 'vue'
import GameGrid from "@/components/GameGrid.vue";
import BackgroundEffect from "@/components/BackgroundEffect.vue";
import Leaderboard from "@/components/Leaderboard.vue";

const message = ref('Chargement...')
const backend_status = ref('down')
const is_initiated = ref(false)
const is_paused = ref(false)
const move_response = ref(false)
const game_grid = ref([[0,0,0,0],[0,2048,2048,0],[0,2048,2048,0],[0,0,0,0]])
const game_won=ref(false)
const game_lose=ref(false)
const game_score=ref(0)
const game_continue_after_won=ref(false)
const current_leaderboard = ref([])

const player_pseudo=ref('')

// API /api/solo/get_grid
async function update_grid() {
  try {
    const response = await fetch('/api/solo/get_grid')
    const data = await response.json()

    // Update all tiles based on the grid returned
    game_grid.value=data;
    return data;
    // backend_status.value = data.grid
  } catch (error) {
    message.value = "Update error"
  }
}

// API /api/solo/get_score
async function update_score() {
  try {
    const response = await fetch('/api/solo/get_score')
    const data = await response.json()

    // Update all tiles based on the grid returned
    game_score.value=data.score;
    return data;
    // backend_status.value = data.grid
  } catch (error) {
    message.value = "Update error"
  }
}

// API /api/solo/init
// API /api/solo/move
async function move_api_request(dir) {

  // If the game is not initialized yet
  if(!is_initiated.value){
    // Initiate the game
    try {
      const response = await fetch('/api/solo/init')
      const data = await response.json()
      is_initiated.value = data.boolean
    } catch (error) {
      message.value = "Erreur de connexion au backend"
    }
    is_initiated.value=true;
    return
  }

  // -------------
  // If the game has started
  try {
    const response = await fetch('/api/solo/move', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({direction: dir})
    })
    const data = await response.json()

    // i.e data={'has_moved': true, 'game_ended':false, 'has_won':true}
    if(data.game_ended){
      game_new_state(data.game_ended,data.has_won)
    }
    if(data.has_won){
      game_new_state(data.game_ended,data.has_won)
    }
  } catch (error) {
    message.value = "Erreur du move up"
  }
}

function game_pause() {
  window.removeEventListener('keydown',handleKeyDown)
  is_paused.value=true
}

function game_resume() {
  window.addEventListener('keydown',handleKeyDown)
  is_paused.value=false
}

function game_continue(){
  game_continue_after_won.value=true;
  game_resume()
}

// API /api/solo/save_score
async function save_score() {
  if(player_pseudo.value.length>0){
    try {
      const response = await fetch('/api/solo/save_score', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({pseudo: player_pseudo.value, score: game_score.value})
      })
      const data = await response.json()
      if (data.success) {
        await update_leaderboard();
      } else {
        console.log("Erreur lors de la mise à jour")
      }
    } catch (error) {
      message.value = "Erreur du move up"
    }
  }
}

async function update_leaderboard() {
  const response = await fetch('/api/solo/get_leaderboard');
  const data = await response.json();

  current_leaderboard.value = data;
}

// API /api/solo/game_reset
async function game_reset() {
  try {
    const response = await fetch('/api/solo/game_reset')
    const data = await response.json()
    if(data.is_reset===true){
      await update_grid()
      await update_score()
      is_paused.value=false;
      game_won.value=false;
      game_lose.value=false;
      game_resume()
    }
  } catch (error) {
    message.value = "Error"
  }
}

function game_new_state(game_end, has_won) {
  // If the player just won, needs to be stored
  if(!game_won.value && has_won) {
    game_won.value=true;
    removeEventListener('keydown', handleKeyDown)
  }else if(game_end){
    game_lose.value=true;
    removeEventListener('keydown', handleKeyDown)
  }
}

const handleKeyDown = async (event) => {
  // Keep keys from doing there initial jobs to not scroll and use their input
  if (['ArrowUp','ArrowDown','ArrowLeft','ArrowRight'].includes(event.key)){
    event.preventDefault()
  }

  switch (event.key){
    // --------------
    //     Moves
    // --------------
    case 'ArrowUp':
      move_response.value = move_api_request('up');
      await update_grid();
      await update_score();
      break;

    case 'ArrowDown':
      move_response.value = move_api_request('down');
      await update_grid();
      await update_score();
      break;

    case 'ArrowLeft':
      move_response.value = move_api_request('left');
      await update_grid();
      await update_score();
      break;

    case 'ArrowRight':
      move_response.value = move_api_request('right');
      await update_grid();
      await update_score();
      break;

    // --------------
    //     Others
    // --------------
    case 'Escape':
      if(is_paused.value){
        game_resume()
      }else{
        game_pause()
      }
      break;
  }
}

// API /api/solo/is_ready
onMounted(async () => {
  // Check the connexion to the backend
  try {
    const response = await fetch('/api/solo/is_ready')
    const data = await response.json()
    backend_status.value = data.message
  } catch (error) {
    message.value = "Erreur de connexion au backend"
  }

  // If it fails, return to not go further
  if(message.value==="Erreur de connexion au backend"){
    return
  }

  // Event listener
  window.addEventListener('keydown', handleKeyDown);
})

onUnmounted(async () => {
  window.removeEventListener('keydown',handleKeyDown)
})
</script>