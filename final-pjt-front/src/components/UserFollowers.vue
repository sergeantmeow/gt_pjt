<template>
  <div>
    <h3 @click="toggleFollowers" class="follower-title">팔로워</h3>
    <ul v-if="showFollowers" class="list-group">
      <li v-for="follower in paginatedFollowers" :key="follower.id" class="list-group-item">
        <router-link :to="{ name: 'OtherProfileView', params: { username: follower.username } }" class="item">
          {{ follower.username }}
        </router-link>
      </li>
    </ul>
    <div class="pagination" v-if="showFollowers">
      <div class="pagination-buttons">
        <button v-for="page in pageCount" :key="page" @click="changePage(page, $event)" :class="{ active: currentPage === page }">{{ page }}</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = process.env.VUE_APP_API_URL;

export default {
  name: 'UserFollowers',
  data() {
    return {
      followers: [],
      showFollowers: false,
      currentPage: 1,
      followersPerPage: 3,
    };
  },
  props: {
    id: Number,
  },
  computed: {
    paginatedFollowers() {
      const startIndex = (this.currentPage - 1) * this.followersPerPage;
      const endIndex = startIndex + this.followersPerPage;
      return this.followers.slice(startIndex, endIndex);
    },
    pageCount() {
      return Math.ceil(this.followers.length / this.followersPerPage);
    },
  },
  created() {
    this.getFollowers();
  },
  methods: {
    toggleFollowers() {
      this.showFollowers = !this.showFollowers;
    },
    getFollowers() {
      axios({
        method: 'GET',
        url: `${API_URL}/accounts/${this.id}/followers/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
        },
      })
        .then((response) => {
          this.followers = response.data;
          this.showFollowers = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    changePage(page, event) {
      this.currentPage = page;
      event.preventDefault();
    },
  },
};
</script>

<style scoped>
.follower-title {
  transition: transform 0.3s ease;
}
.follower-title:hover {
  transform: scale(1.1);
}

.list-group-item {
  border-color: rgb(31, 32, 63, 0);
  background-color: rgb(31, 32, 63, 0);
  color: #bfbfbf;
}

.list-group-item:hover {
  background-color: rgba(79, 61, 99, 0);
  color: #ff2679;
}

.item {
  color: #bfbfbf;
  text-decoration: none;
}

.item:hover {
  color: #ff2679;
}

.pagination {
  margin-top: 10px;
  display: flex;
  justify-content: center;
}

.pagination-buttons {
  display: flex;
  align-items: center;
}

.pagination button {
  margin: 5px;
  padding: 5px 10px;
  background-color: #fff;
  border: 1px solid #ccc;
  color: #333;
  cursor: pointer;
}

.pagination button:hover {
  background-color: #eee;
}

.pagination button.active {
  background-color: #ff2679;
  color: #fff;
}
</style>