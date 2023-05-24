<template>
  <div v-if="comment" class="comment-container">
    <h6 class="comment-content">{{ comment.content }}</h6>
      <div class="otheruser-link">
      <p>
        <router-link :to="{ name: 'OtherProfileView', params: { username: comment.username } }">
          {{ comment.username }}
        </router-link>
      </p>
      </div>
    <p>{{ formatDateTime(comment.created_at) }}</p>
    <!-- <p>수정일 : {{ formatDateTime(comment.updated_at) }}</p> -->
    <div v-if="isAuthor" class="comment-icons">
      <span class="edit-icon" @click="editComment">
        <img src="@/assets/icon-edit.png" alt="수정 아이콘" class="comment-icon-img">
      </span>
      <span class="delete-icon" @click="deleteComment">
        <img src="@/assets/icon-delete.png" alt="삭제 아이콘" class="comment-icon-img">
      </span>
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
      return `${year}-${month}-${day} ${hours}:${minutes}`;
    },
    deleteComment(){ 
      if (confirm('댓글을 삭제하시겠습니까?')) {
        const id = this.comment.id;
        axios({
          method: 'delete',
          url: `${API_URL}/articles/comments/${ id }/`,
          headers: {
          Authorization: `Token ${this.$store.state.user.token}`
          },
        })
        .then(() => {
          this.$eventBus.$emit('commentDeleted');
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    editComment() {
      const newContent = prompt('댓글 내용을 수정하세요:', this.comment.content);
      if (newContent) {
        const id = this.comment.id;
        axios({
          method: 'put',
          url: `${API_URL}/articles/comments/${id}/`,
          headers: {
          Authorization: `Token ${this.$store.state.user.token}`
          },
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

<style scoped>
.comment-container {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.comment-content {
  margin-bottom: 15px;
  margin-right: 10px;
  word-wrap: break-word;
}

.otheruser-link {
  margin-right: 5px;
}
.comment-icons {
  margin-left: 10px;
  display: flex;
}

.comment-icon-img {
  width: 20px;
  height: 20px;
  transition: transform 0.2s ease-in-out;
  margin-right : 3px;
  margin-bottom: 10px;
}

.comment-icon-img:hover {
  transform: scale(1.3);
}
</style>