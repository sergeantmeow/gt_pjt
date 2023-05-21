<template>
  <div v-if="comment">
    <hr>
    <h5>{{ comment.content }}</h5>
    <p>작성자 : 
      <router-link :to="{ name: 'OtherProfileView', params: { username: comment.username } }">
        {{ comment.username }}
      </router-link>
    </p>
    <p>작성일 : {{ comment.created_at }}</p>
    <p>수정일 : {{ comment.updated_at }}</p>
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
    // 댓글 단방향말고 양방향으로 만들기 위해서 props 제거하기
    // getComment(){
    //   const id = this.comment.id;
    //   axios({
    //       method: 'get',
    //       url: `${API_URL}/articles/comments/${ id }/`
    //     })
    //     .then((respons) => {
          
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
    deleteComment(){ 
      if (confirm('댓글을 삭제하시겠습니까?')) {
        const id = this.comment.id;
        axios({
          method: 'delete',
          url: `${API_URL}/articles/comments/${ id }/`
        })
        .then(() => {
          location.reload();
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
          location.reload();
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