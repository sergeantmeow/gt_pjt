<template>
  <div>
    <h1>Home Page</h1>
    <router-link :to="{ name: 'ArticleView' }">[Articles]</router-link>
    <ArticleList />
    <hr>
  </div>
</template>

<script>

export default {
  name: 'HomeView',
}
</script>

<style>

</style>
