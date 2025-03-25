<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div class="bg-blue-500 text-red p-6 font-semibold py-5">Tailwind działa poprawnie!</div>
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
<script setup lang="ts"></script>
