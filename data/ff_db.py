import mysql.connector



class FFDB(object):
    def __init__(self, database='', host='', username='', password=''):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    def connect_to_db(self):
        """
        @description: Connects to db. Returns a Database connection.
        """
        mydb = mysql.connector.connect(
            host=self.host,
            username=self.username,
            password=self.password,
            database=self.database
        )

        return mydb
    
    def create_database(self):
        """
        @description: Creates tables if they don't exist already.
        """
        mydb = self.connect_to_db()
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE winners_circle_ff")

    def create_tables(self):
        """
        @description: Creates tables if they don't exist already.
        """
        mydb = self.connect_to_db()
        mycursor = mydb.cursor()


   
        # player_columns = """
        #         (gsis_id VARCHAR(50),
        #         depth_chart_position VARCHAR(30),
        #         position VARCHAR(10),
        #         depth_chart_order INT,
        #         college VARCHAR(50),
        #         birth_country VARCHAR(50),
        #         birth_city VARCHAR(50),
        #         weight VARCHAR(10),
        #         first_name VARCHAR(50),
        #         birth_date VARCHAR(30),
        #         espn_id INT,
        #         age INT,
        #         stats_id INT,
        #         yahoo_id INT,
        #         rotowire_id INT,
        #         player_id VARCHAR(50),
        #         search_last_name VARCHAR(50),
        #         sportradar_id VARCHAR(100),
        #         years_exp INT,
        #         injury_start_date VARCHAR(30),
        #         injury_body_part VARCHAR(255),
        #         rotoworld_id INT,
        #         last_name VARCHAR(50),
        #         number INT,
        #         sport VARCHAR(10),
        #         team VARCHAR(30),
        #         full_name VARCHAR(50),
        #         height VARCHAR(30),
        #         practice_description TEXT,
        #         birth_state VARCHAR(30),
        #         active BOOL,
        #         news_updated INT,
        #         hashtag VARCHAR(100),
        #         fantasy_data_id INT,
        #         search_first_name VARCHAR(50),
        #         search_full_name VARCHAR(50),
        #         status VARCHAR(30),
        #         search_rank INT,
        #         injury_notes TEXT,
        #         high_school VARCHAR(50),
        #         injury_status VARCHAR(30))
        #         """
    
        # mycursor.execute("CREATE TABLE players " + player_columns)


        weekly_player_stats_columns = """
            (bonus_rush_rec_yd_100 FLOAT,
            bonus_rec_yd_100 FLOAT,
            bonus_rec_wr FLOAT,
            cmp_pct FLOAT,
            fum_lost FLOAT,
            fum FLOAT,
            gs FLOAT,
            gp FLOAT,
            gms_active FLOAT,
            humidity FLOAT,
            off_snp FLOAT,
            rec_ypt FLOAT,
            rec_ypr FLOAT,
            rec_yd FLOAT,
            rec_tgt FLOAT,
            rec_td FLOAT,
            rec_pct FLOAT,
            rec_lng FLOAT,
            rec_fd FLOAT,
            rec_5_9 FLOAT,
            rec_30_39 FLOAT,
            rec_20_29 FLOAT,
            rec_10_19 FLOAT,
            rec FLOAT,
            rush_ypa FLOAT,
            rush_yd FLOAT,
            rush_td FLOAT,
            rush_att FLOAT,
            pts_std FLOAT,
            pts_ppr FLOAT,
            pts_half_ppr FLOAT,
            pass_ypc FLOAT,
            pass_ypa FLOAT,
            pass_yd FLOAT,
            pass_td_40p FLOAT,
            pass_td FLOAT,
            pass_rtg FLOAT,
            pass_int FLOAT,
            pass_inc FLOAT,
            pass_fd FLOAT,
            pass_cmp_40p FLOAT,
            pass_cmp FLOAT,
            pass_att FLOAT,
            player_id VARCHAR(50),
            season INT,
            tm_st_snp FLOAT,
            tm_off_snp FLOAT,
            tm_def_snp FLOAT,
            temperature FLOAT,
            td FLOAT,
            week INT,
            wind_speed FLOAT)
            """
        mycursor.execute("CREATE TABLE weekly_player_stats " + weekly_player_stats_columns)

    def insert_players(self, players):
        """
        @description: Creates tables if they don't exist already.
        """
        mydb = self.connect_to_db()

        sql = """INSERT INTO players (
                gsis_id,
                depth_chart_position,
                position,
                depth_chart_order,
                college,
                birth_country,
                birth_city,
                weight,
                first_name,
                birth_date,
                espn_id,
                age,
                stats_id,
                yahoo_id,
                rotowire_id,
                player_id,
                search_last_name,
                sportradar_id,
                years_exp,
                injury_start_date,
                injury_body_part,
                rotoworld_id,
                last_name,
                number,
                sport,
                team,
                full_name,
                height,
                practice_description,
                birth_state,
                active,
                hashtag,
                fantasy_data_id,
                search_first_name,
                search_full_name,
                status,
                search_rank,
                injury_notes,
                high_school,
                injury_status
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        try:
            mycursor = mydb.cursor()

            mycursor.executemany(sql, players)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            print('Error: ', e)
            mydb.rollback()
        finally:
            mycursor.close()



    def insert_weekly_player_stats(self, weekly_player_stats):
        """
        @description: Creates tables if they don't exist already.
        """
        mydb = self.connect_to_db()

        sql = """INSERT INTO weekly_player_stats (
                bonus_rush_rec_yd_100,
                bonus_rec_yd_100,
                bonus_rec_wr,
                cmp_pct,
                fum_lost,
                fum,
                gs,
                gp,
                gms_active,
                humidity,
                off_snp,
                rec_ypt,
                rec_ypr,
                rec_yd,
                rec_tgt,
                rec_td,
                rec_pct,
                rec_lng,
                rec_fd,
                rec_5_9,
                rec_30_39,
                rec_20_29,
                rec_10_19,
                rec,
                rush_ypa,
                rush_yd,
                rush_td,
                rush_att,
                pts_std,
                pts_ppr,
                pts_half_ppr,
                pass_ypc,
                pass_ypa,
                pass_yd,
                pass_td_40p,
                pass_td,
                pass_rtg,
                pass_int,
                pass_inc,
                pass_fd,
                pass_cmp_40p,
                pass_cmp,
                pass_att,
                player_id,
                season,
                tm_st_snp,
                tm_off_snp,
                tm_def_snp,
                temperature,
                td,
                week,
                wind_speed
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        try:
            mycursor = mydb.cursor()

            mycursor.executemany(sql, weekly_player_stats)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        except Exception as e:
            print('Error: ', e)
            mydb.rollback()
        finally:
            mycursor.close()