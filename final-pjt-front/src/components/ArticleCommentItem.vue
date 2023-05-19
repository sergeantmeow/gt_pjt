<template>
  <div>
    <h5>{{ comment.content }}</h5>
    <div v-if="comment">
    <p>작성자 : 
      <router-link :to="{ name: 'OtherProfileView', params: { username: comment.username } }">
        {{ comment.username }}
      </router-link>
    </p>
  </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleCommentItem',
  props: {
    comment: Object,
  }
}

</script>

<style>
</style>