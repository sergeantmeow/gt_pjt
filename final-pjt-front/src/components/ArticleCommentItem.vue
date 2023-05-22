<template>
  <div v-if="comment">
    <hr>
    <h5>댓글: {{ comment.content }}</h5>
    <p>작성자 : 
      <router-link :to="{ name: 'OtherProfileView', params: { username: comment.username } }">
        {{ comment.username }}
      </router-link>
    </p>
    <p>작성일 : {{ formatDateTime(comment.created_at) }}</p>
    <!-- <p>수정일 : {{ formatDateTime(comment.updated_at) }}</p> -->
    <div v-if="isAuthor">
      <button @click="editArticle">수정</button>
      <button @click="deleteComment">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCommentItem',
  props: {
    comment: Object,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    currentUser(){
      return this.$store.getters.currentUser
    },
    isAuthor() {
      return this.isLogin && this.comment?.username === this.currentUser.username
    },
  },
  methods: {
    formatDateTime(dateTime) {
      if (!dateTime) return '';

      const date = new Date(dateTime);
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      const seconds = date.getSeconds().toString().padStart(2, '0');

      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
    deleteComment(){ 
      if (confirm('댓글을 삭제하시겠습니까?')) {
        const id = this.comment.id;
        axios({
          method: 'delete',
          url: `${API_URL}/articles/comments/${ id }/`
        })
        .then(() => {
          this.$eventBus.$emit('commentDeleted');
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    editArticle() {
      const newContent = prompt('댓글 내용을 수정하세요:', this.comment.content);
      if (newContent) {
        const id = this.comment.id;
        axios({
          method: 'put',
          url: `${API_URL}/articles/comments/${id}/`,
          data: {
            content: newContent
          }
        })
        .then(() => {
          this.$eventBus.$emit('commentDeleted');
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
  }
}

</script>

<style>
</style>