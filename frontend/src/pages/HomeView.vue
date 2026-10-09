<template>
  <!-- Flowbite component -->
  <fwb-jumbotron
    header-text="2048 Online"
    sub-text="On a tous déjà rêvé de jouer à un 2048 avec ses ami·e·s non ? Non ? Qu'importe, maintenant que tu es là, viens jouer !"
    class="mt-30 opacity-90 backdrop-blur-xl"
    id="test"
  >
    <!-- Buttons -->
    <div class="flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0">
      <RouterLink to="solo"
                  class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-512
                  hover:bg-4096 focus:ring-4 dark:focus:ring-blue-900">
        Jouer seul
      </RouterLink>

      <RouterLink to="coop"
                  class="inline-flex justify-center items-center py-3 px-5 sm:ml-4 text-base font-medium text-center text-gray-900 rounded-lg border border-gray-300
        hover:bg-2 focus:ring-gray-100 dark:text-white dark:border-gray-700 dark:hover:bg-gray-700 dark:focus:ring-gray-800">
        Jouer en ligne
      </RouterLink>
    </div>
  </fwb-jumbotron>
</template>

<script setup>
  import { FwbJumbotron } from 'flowbite-vue'
  import {RouterLink} from "vue-router";
  import {onMounted, onUnmounted, ref} from "vue";

  const windowWidth = ref(0);
  const windowHeight = ref(0);
  const body = ref();
  const amountDecoration = 50;
  const images=["2","4","8","16","32","64","128","256","512","1024","2048","4096"]

  function updatedPageSize(){
    windowWidth.value=window.innerWidth;
    windowHeight.value=window.innerHeight;
  }

  function addBackgroundEffect(){
    let i=0;

    while(i<amountDecoration){
      const img = document.createElement('img');
      const numberImg = 2**(1+Math.floor(Math.random()*(images.length-1)));

      const posX=Math.floor(Math.random()*windowWidth.value-50);
      const posY=Math.floor(Math.random()*windowHeight.value-50);

      const size=Math.floor(Math.random()*50)+10;
      const delay=Math.random()*-20;
      const duration=Math.random()*5;

      img.src="src/assets/"+numberImg+".svg";
      img.className="decoration";

      img.style.position="absolute";
      img.style.left=posX+'px';
      img.style.top=posY+'px';
      img.style.width=size+'px';
      img.style.animationDelay=delay+'s';
      img.style.duration=duration+'s';
      body.value.appendChild(img);
      i++;
    }
  }

  function removeBackgroundEffect(){
    for(let i=0;i<amountDecoration;i++){
      const element = document.getElementsByClassName('decoration');
      element.item(0).remove();
    }
  }
  onMounted(()=>{
    body.value = document.getElementById('app');
    updatedPageSize();
    addBackgroundEffect();
  });

  onUnmounted(() => {
    removeBackgroundEffect();
  })

  window.addEventListener("resize", () => {
    removeBackgroundEffect();
    updatedPageSize();
    addBackgroundEffect();
  })
</script>

<style>
.decoration {
  z-index: -1;
  animation: animate 5s linear infinite;
}

@keyframes animate {
  0% {
        opacity: 0;
        transform: scale3d(.3, .3, .3)
    }
    50% {
        opacity: 1
    }
  100% {
    opacity: 0;
  }
}
</style>