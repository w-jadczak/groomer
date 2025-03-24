<template>
  <nav>
    <router-link to="/">Home</router-link>
  </nav>
  <router-view />
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
