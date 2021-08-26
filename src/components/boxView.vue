<template>
  <div class="boxView">
      <div class="loading" v-if="state">
        <img src="../assets/loader.svg">
      </div>
      <div class="data" v-if="!state && content">
        <img :src="'http:'+content.current.condition.icon">
        <div class="content">
          <span class="city"><span class="indicator">Ville</span>      {{content.location.name}}</span><br>
          <span class="temp"><span class="indicator">Temperature</span>      {{content.current.temp_c}} °c</span><br>
          <span class="sky"><span class="indicator">Ciel</span>       {{content.current.condition.text}}</span><br>
          <span class="wind"><span class="indicator">Vent</span>       {{content.current.vis_miles}} km</span>
        </div>
      </div>
  </div>
</template>
<script setup>
import { inject,  watch } from "@vue/runtime-core";

const content = inject("content")
const state = inject("state") 
watch(content,(_,ne)=>{
  console.log(ne)
})
</script>
<style>
.boxView{
    width:50%;
    height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    border-radius: 10px;
}

.loading{
  display: flex;
  align-items: center;
  justify-content: center;
}
.loading img{
  animation: rotor 3s infinite;
  width: 200px;
  height: auto;
  
}
@keyframes rotor{
  from{
    transform: rotate(0deg);
  }
  to{
    transform: rotate(360deg);
  }
}
.data{
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
}
.data img{
  float: left;
  width: 100px;
  object-fit: contain;
}
span.indicator{
  font-weight: bolder;
}
div.content{
  width: 90%;
  display: flex;
  align-items: center;
  flex-direction: column;
}
div.content>span{
  width: 100%;
  padding-left: 30%;
}
@media screen and (max-width:680px) {
  div.content>span{
    padding-left:20% ;
  }
  .boxView{
    width: 95%;
  }
}
</style>