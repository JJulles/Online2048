<template>

</template>

<script setup>
  import {onMounted, onUnmounted, ref} from "vue";

  const props = defineProps({
    amountDecoration:Number,
    duration:Number
  })

  const windowWidth = ref(0);
  const windowHeight = ref(0);
  const body = ref();
  const images=["2","4","8","16","32","64","128","256","512","1024","2048","4096"]

  function updatedPageSize(){
    windowWidth.value=window.innerWidth;
    windowHeight.value=window.innerHeight;
  }

  function addBackgroundEffect(){
    let i=0;

    while(i<props.amountDecoration){
      const img = document.createElement('img');
      const numberImg = 2**(1+Math.floor(Math.random()*(images.length-1)));

      const posX=Math.floor(Math.random()*windowWidth.value-50);
      const posY=Math.floor(Math.random()*windowHeight.value-50);

      const size=Math.floor(Math.random()*50)+10;
      const delay=Math.random()*-20;

      img.src="src/assets/"+numberImg+".svg";
      img.className="decoration";

      img.style.position="absolute";
      img.style.left=posX+'px';
      img.style.top=posY+'px';
      img.style.width=size+'px';
      img.style.animationDelay=delay+'s';

      const duration = props.duration || 5;
      img.style.setProperty('--anim-duration', duration + 's');

      body.value.appendChild(img);
      i++;
    }
  }

  function removeBackgroundEffect(){
    for(let i=0;i<props.amountDecoration;i++){
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
  animation: animate var(--anim-duration, 5s) linear infinite;
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