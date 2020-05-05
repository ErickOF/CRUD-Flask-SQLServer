SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- ====================================================
-- Author:      Erick Andres Obregon Fonseca
-- Create date: 5th May 2020
-- Description: Return an user who matches with UserID
-- ====================================================

CREATE PROCEDURE getUserByID
    @UserID int
AS
BEGIN
    SET NOCOUNT ON;

    SELECT * FROM [user] WHERE [user].id_user = @UserID;
END
GO
